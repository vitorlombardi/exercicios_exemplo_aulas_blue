const mongoose = require("mongoose")



const ProdutoSchema = new mongoose.Schema({

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

//const Filme = mongoose.model('Filme', FilmeSchema);

//module.exports = Filme

module.exports = mongoose.model("legumes", ProdutoSchema);