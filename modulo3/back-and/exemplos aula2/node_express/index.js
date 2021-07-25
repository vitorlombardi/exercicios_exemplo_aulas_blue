const express = require('express') //importando espress
const app = express(); // iniciando o express

app.get('/', (req,res)=>{

    res.send("Batata");

});

app.get('/blue', (req,res)=>{

    res.send('<h1> bem vindo a <b>BATATA AZUL</b></h1>');

});

app.get('/blue/info', (req,res)=>{

    res.send('<h2><b>BATATA</b> no node.js</h2>');

});

app.listen(4000, function(erro){

    if (erro){
        console.log('deu ruim, da seus pulo para resolver')
    }else{
        console.log('deu bom, servidor iniciado com sucesso')
    }
});

