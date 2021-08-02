const express = require("express");

const app = express();
const port = 3001;
app.use(express.json());

const mongoose = require("mongoose");
const legumes = require("./models/legumes");

mongoose.connect("mongodb://localhost:27017/legumes", {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

app.get("/", (req, res) => {
  res.send("ola batata");
});

app.get("/legumes", async (req, res) => {
  const legume = await legumes.find();
  res.send(legume);
});

app.get("/legumes/:id", async (req, res) => {
  try {
    const legume = await legumes.findById(req.params.id);
    if (legume == null) {
      return res
        .status(404)
        .send({ message: "Não é possível encontrar o legume." });
    }
    res.send(legume);
  } catch (err) {
    return res.status(500).send({ message: err.message });
  }
});

app.post("/legumes", async (req, res) => {
  const legume = new legumes({
    nome: req.body.nome,
    imagem_url: req.body.imagem_url,
  });

  // Validação

  if (!legume || !legume.nome || !legume.imagem_url) {
    res.status(400).send({
      message:
        'legume inválido. Certifique-se de que o body da requisição possui "nome" e "url".',
    });

    return;
  }

  const legume_Salvo = await legume.save();
  res.send(legume_Salvo);
});

app.put("/legumes/:id", async (req, res) => {
  try {
    const legume = await legumes.findByIdAndUpdate(req.params.id);
    const novo_legume = req.body;

    if (novo_legume.nome && novo_legume.imagem_url != null) {
      legume.nome = novo_legume.nome;
      legume.imagem_url = novo_legume.imagem_url;
    } else {
      return res.status(400).send({
        message:
          "Não foi possivel realizar sua reqisição. Verifique os capos e tente novamente",
      });
    }
    const legume_update = await legume.save();
    res.send(legume_update);
  } catch (err) {
    return res.status(500).send({ message: err.message });
  }
});

app.delete("/legumes/:id", async (req, res) => {
  try {
    const legume = await legumes.findById(req.params.id);

    if (legume == null) {
      return res.status(404).send({ message: "Legume não foi encontrado" });
    }

    await legume.remove();
    res.send({ message: "legume excluido com sucesso" });
  } catch (err) {
    return res.status(500).send({ message: err.message });
  }
});

app.listen(port, () => {
  console.info(`App codando em: http://localhost:${port}`);
});
