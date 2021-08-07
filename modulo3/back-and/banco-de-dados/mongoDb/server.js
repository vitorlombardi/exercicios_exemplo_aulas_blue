const express = require("express")
const mongoose = require("mongoose")
const comidaRoute = require("../mongoDb/routes/comidaRoute.js")

const port = 3001

const App = express();
App.use(express.json());
App.use(comidaRoute);

mongoose.connect(
    "mongodb+srv://jorginho:uNr6D3M0EOicmYd5@serverestudo.nnq4e.mongodb.net/test",
    {
        useNewUrlParser:true,
        useUnifiedTopology:true
    }
);

App.listen(port, () =>{
    console.log(`sevidor rodando na porta: htts://localhost:${port}`)
})

