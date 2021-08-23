const  plantaModel = require('./../models/plantas');


class PlantaService {

    async findAll(){
        return await plantaModel.find();
    }
    async findById(id){
        return await plantaModel.findById(id);
    } 
    async createPlanta(planta){
        return await new plantaModel(planta).save()
    }
    async updatePlanta(planta, id){
        return await plantaModel.findByIdAndUpdate({_id:id}, planta)
    }
    async deletePlanta(id){
        return await plantaModel.findByIdAndDelete(id)
    }
};

module.exports =  PlantaService;