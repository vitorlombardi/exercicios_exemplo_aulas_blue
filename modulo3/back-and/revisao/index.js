const express = require("express");
const mongoose = require("mongoose");
const plantaRouter = require("./routes/planta.router") 

const app = express();
const port = 3001;

app.use(express.json());
app.use(plantaRouter);


mongoose.connect('mongodb://localhost:27017/db_Plantas', {
    useUnifiedTopology:true,
    useNewUrlParser:true
})


app.get("/", (req, res) => {
    res.send("Batata, você e meu amor")
});

app.listen(port, () =>{
    console.info(`app rodando na em: http://localhost:${port}`)
});