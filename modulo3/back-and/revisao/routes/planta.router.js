const PlantaControler = require("../controllers/planta.controller");
const express = require("express");
const router = express.Router();

const plantaControler = new PlantaControler();

router.get("/plantas", plantaControler.getAllPlantas);

router.get("/plantas/:id", plantaControler.getPlantaId);

router.post("/plantas", plantaControler.createPlanta);

router.put("/plantas/:id", plantaControler.updatePlanta);

router.delete("/plantas/:id", plantaControler.deletePlanta);

module.exports = router;