const mongoose = require("mongoose");

const ComidaSchema = new mongoose.Schema({
    nome:{
        type: String,
        required: true,
        trim: true,
        lowercase:true
    },

    caloria:{
        type: Number,
        default: 0,
        validate(value){
            if(value <0) 
            throw new error("você é burro ou se faz, não existe calorias negativas");
        } 
    }
});

const Comida = mongoose.model("Comida", ComidaSchema);

module.exports = Comida