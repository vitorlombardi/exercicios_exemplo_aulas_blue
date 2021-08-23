const PlantaService = require("./../services/planta.service");
const mongoose = require("mongoose")
const model = require("./../models/plantas") 

const plantaService = new PlantaService();

class PlantaControler {
    async getAllPlantas(req, res){
        const plantas = await plantaService.findAll();
        res.send(plantas)
    }
    async getPlantaId(req, res){
        const id = req.params.id;

        if (!mongoose.Types.ObjectId.isValid(id)){
            res.status(422).send("id invalido")
            return;
        }

        const planta = await plantaService.findById(id)
        
        if (!planta){
            res.status(404).send({message:"planta não encontrada"});
            return;
        }
        res.send(planta);
    }
    async createPlanta(req, res){
        const planta = req.body;

        if(planta.lenght < model.lenght){
            res.sendStatus(400).send({message:"verifique se o body da requisição possui todos os campos necessários: 'nome', 'tipo','ImagemUrl','alimento'."});
            return;
        }
    
        if(planta.alimento === true || planta.alimento === false){
            const plantaSalva = await plantaService.createPlanta(planta);
    
            res.send(plantaSalva)
        }else{
            res.send({messsage:"Certifique-se que o valor passado para o alimento é BOLEANO!"})
            return;
        }
        
    }
    async updatePlanta(req, res){
        const id = req.params.id;
        if (!mongoose.Types.ObjectId.isValid(id)){
            res.status(422).send("id invalido")
            return;
        }

        const planta = await plantaService.findById(id);
        if (!planta){
            res.status(404).send({message:"planta não encontrada"});
            return;
        }

        const novaPlanta = req.bory;
        if(!novaPlanta || planta.lenght !== novaPlanta.lenght ){
            res.status(400).send("Certifique-se que o body da requisição possui todos os dados: 'nome', 'tipo','ImagemUrl','alimento'.")
            return;
        }
        
        plantaService.updatePlanta(novaPlanta, id);
        const plantaSalva = await plantaSalva.findById(id);
        res.send(plantaSalva);
    }
    async deletePlanta(req, res){
        const id = req.params.id;
        if (!mongoose.Types.ObjectId.isValid(id)){
            res.status(422).send("id invalido")
            return;
        }
        
        const planta = await plantaService.findById(id);
        if (!planta){
            res.status(404).send({message:"planta não encontrada"});
            return;
        }

        await plantaService.deletePlanta(id);

        res.send({message:"planta excluida com sucesso"})


    }
    
};

module.exports = PlantaControler;