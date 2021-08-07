const produtoModel = require("./../models/produtos");

class ProdutoService {
    async findAll() {
        return await produtoModel.find();
    }

    async findById(id) {
        return await produtoModel.findById(id);
    }

    async createProduto(legumes) {
        return await new produtoModel(legumes).save(id);
    }

    async updateFilme(legume, id) {
        return await produtoModel.findOneAndUpdate({_id: id}, legume);
    }

    async delete(id) {
        return await produtoModel.findByIdAndDelete(id);
    }
};

module.exports = ProdutoService;