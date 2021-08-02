const mongoose = require("mongoose")

const legumes_model = new mongoose.Schema({
    nome: {type: String, require: true},
    url: {type: String, require: true}
});

module.exports = legumes_model;