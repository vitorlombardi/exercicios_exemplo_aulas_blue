//import express
const express = require("express");

// import do mongoose
const mongoose = require("mongoose")

//impor model

const legumes_model = require("./models/legumes")

//url de conexão
// useNewUrlParser -> novo siatema de url
//useUnifiedTopology ->permisao para monitorar o banco de dados

mongoose.connect("mongodb://localhost:27017/legumes",{
    useUnifiedTopology: true,
    useNewUrlParser: true
});

const Legume = mongoose.model("legume", legumes_model)// pega o schema , prepara o model  e retorna um objeto

/*//adicionado legumes
 const item = new Legume({
     nome:'Rúcula',
     url:'https://s3.static.brasilescola.uol.com.br/be/2021/02/rucula.jpg'
   });*/

/* item.save().then(() => { // condição de sucesso
     console.log("legume salvo");
 }).catch((err)=>{
    console.log(err);
 });*/

//listar os legumes
/*
Legume.find({}).then((legumes) => {
    console.log(legumes);
}).catch((err) => {
    console.log(err);
});*/

// update 

/*Legume.findByIdAndUpdate("60ff1c1b1a1055221481dc90",{
    nome:'Rúcula',
    url:'https://s3.static.brasilescola.uol.com.br/be/2021/02/rucula.jpg'
}).then(() => { // condição de sucesso
    console.log("legume atualizado com sucesso");
}).catch((err)=>{
   console.log(err);
});*/

//delete
/*
Legume.findByIdAndDelete("60ff1c1b1a1055221481dc90").then(() => { 
    console.log("Legume deletado com sucesso");
}).catch((err)=>{
   console.log(err);
});*/






const app = express();
const port = 3001;

// [Get]
app.get("/",(req,res) =>{
    res.send('ola mundo!')
})



app.listen (port, () => {
    console.info(`App rodando em: http://localhost:${port} `)
});