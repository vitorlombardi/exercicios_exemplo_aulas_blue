const mongoose = require("mongoose")



const legumes_schema = new mongoose.Schema({

    nome:{
        type: String,
        require: true
    },
    imagem_url:{
        type: String,
        require: true
    },
    created_al:{
        type: Date,
        require: true,
        default: Date.now
    }


});

module.exports = mongoose.model("legumes", legumes_schema);