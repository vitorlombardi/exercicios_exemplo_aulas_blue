const express = require('express');
const cors = require("cors")
const mongoose = require("mongoose")
const quitandaRoutes = require("./routes/quitanda.routes.js")

mongoose.connect("mongodb://localhost:27017/legumes", {
    useNewUrlParser: true,
    useUnifiedTopology: true
});

const corsOptions = {
    origin:"http://localhost:3000",
    optionsSuccessStatus: 200
};

const app = express();
app.use(express.json());
app.use(cors(corsOptions))
app.use(quitandaRoutes);
const port = 5000;


app.get('/', (req, res) => {
    res.send('Ola blumer');
});

app.listen(port, () => {
    console.info(`App codando em: http://localhost:${port}`);
});



