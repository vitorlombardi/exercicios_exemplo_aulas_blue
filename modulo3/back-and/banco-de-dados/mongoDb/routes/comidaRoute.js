const express = require("express")
const comidaModel = require("../models/comida")

const app = express();

app.get("/comidas", async (req, res) => {
    const comidas = await comidaModel.find({});

    try {
        return res.send(comidas)
    }catch (error){
        res.status(500).send(error);
    }
});

app.get("/comidas/:id", async (req, res) => {
    try{
        const comida = await comidaModel.findById(req.params.id);
        res.send(comida);
    }catch (error) {
        res.status(404).send(error);
    }
});

app.post("/comidas", async (req, res) => {
    const comida = new comidaModel(req.body)

    try{
        const comidaSalva =  await comida.save();
        res.send(comidaSalva);
    }catch (error){
        res.status(400).send(error)
    }
});



module.exports = app;