const express = require("express")
const mongoose = require("mongoose")

const port = 3001

const App = express();
App.use(express.json());

mongoose.connect(
    "mongodb+srv://jorginho:CiESqbvFkCqIY7Ta@cluster0.nnq4e.mongodb.net/test",
    {
        useNewUrlParser:true,
        useUnifiedTopology:true
    }
);

App.listen(port, () =>{
    console.log(`sevidor rodando na porta: htts://localhost:${port}`)
})

