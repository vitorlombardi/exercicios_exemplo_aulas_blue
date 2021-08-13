const ProdutosService = require("./../Services/quitanda.Services")
const mongoose = require("mongoose")

const produtoService = new ProdutosService();

class ProdutosControler {
    async getProdutos(req, res) {
        const produtos = await produtoService.findAll();
        res.send(produtos);
        }

        async getProdutoById(req, res) {
        const id = req.params.id;

        if (!mongoose.Types.ObjectId.isValid(id)) {
            res.status(422).send("produto inválido.");
            return;
        }

        const produto = await produtoService.findById(id);

        if (!produto) {
            res.status(404).send("produto não encontrado.");

            return;
        }

        res.send(produto);
        }

        async createProduto(req, res) {
        const produto = req.body;
        console.log(produto)

        if (!produto || !produto.nome || !produto.imagemUrl || !produto.valor || !produto.tipo) {
            console.log("bao")
            res.status(400).send({
            message:
                'produto inválido. Certifique-se de que o body da requisição possui todos os dados.',
            });

            return;
        }

        const produtoSalvo = await produtoService.createProduto(produto);

        res.send(produtoSalvo);
        }

        async updateProduto(req, res) {
        const id = req.params.id;

        if (!mongoose.Types.ObjectId.isValid(id)) {
            res.send("produto inválido.");
            return;
        }

        const produto = await produtoService.findById(id);

        if (!produto) {
            res.status(404).send("produto não encontrado.");

            return;
        }

        const novoProduto = req.body;

        if (!Object.keys(novoProduto).length) {
            res.status(400).send({ message: "O body da requisição está vazio." });

            return;
        }

        if (!produto || !produto.nome || !produto.imagemUrl || !produto.valor || !produto.tipo) {
            res.status(400).send({
            message:
                'produto inválido. Certifique-se de que o body da requisição possui todos os dados".',
            });

            return;
        }

        produtoService.updateProduto(novoProduto, id);
        const produtoAtualizado = await produtoService.findById(id);

        res.send(produtoAtualizado);
        }

        async deleteProduto(req, res) {
        const id = req.params.id;

        if (!mongoose.Types.ObjectId.isValid(id)) {
            res.status(422).send("Código inválido.");
            return;
        }

        const produto = await produtoService.findById(id);

        if (!produto) {
            res.status(404).send("produto não encontrado.");

            return;
        }

        await produtoService.delete(id);

        res.send({ message: "produto excluído com sucesso" });
        }
}

    module.exports = ProdutosControler;
    
