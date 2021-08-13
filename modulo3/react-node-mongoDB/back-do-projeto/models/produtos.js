const mongoose = require("mongoose")



const ProdutoSchema = new mongoose.Schema({

    nome:{
        type: String,
        require: true
    },
    imagemUrl:{
        type: String,
        require: true
    },
    tipo:{
        type: String,
        require: true
    },
    valor:{
        type: String,
        require: true,
        validate(value){
            if(value <0) 
            throw new error("Por favor insira um valor para o produto");
        } 
    },
    promocao:{
        type: String,
        default:"não"
    }
});

const Produto = mongoose.model("produto", ProdutoSchema);

module.exports = Produto

