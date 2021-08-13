const produtoModel = require("./../models/produtos");

class ProdutoService {
    async findAll() {
        return await produtoModel.find();
    }

    async findById(id) {
        return await produtoModel.findById(id);
    }

    async createProduto(produto) {
        return await new produtoModel(produto).save();
    }

    async updateProduto(produto, id) {
        return await produtoModel.findOneAndUpdate({_id: id}, produto);
    }

    async delete(id) {
        return await produtoModel.findByIdAndDelete(id);
    }
};

module.exports = ProdutoService;