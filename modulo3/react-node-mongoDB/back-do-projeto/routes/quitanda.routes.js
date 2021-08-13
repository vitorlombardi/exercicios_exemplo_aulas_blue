const express = require("express");
const QuitandaController = require("./../controllers/quitanda.controlles");

const router = express.Router();
const produtoController = new QuitandaController();


router.get("/produtos", produtoController.getProdutos);

router.get("/produtos/:id", produtoController.getProdutoById);

router.post("/produtos", produtoController.createProduto);

router.put("/produtos/:id", produtoController.updateProduto);

router.delete("/produtos/:id", produtoController.deleteProduto);

module.exports = router;