const mongoose = require("mongoose")

const PlantasSchema = new mongoose.Schema({
    nome:{
        type:String,
        required:true,
    },
    tipo:{
        type:String,
        required:true,
    },
    imagemUrl:{
        type:String,
        required:true,
    },
    alimento:{
        type:Boolean,
        required:true
    },
}); 

const Planta = mongoose.model("db_Plantas", PlantasSchema);

module.exports = Planta;