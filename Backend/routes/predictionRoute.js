const express = require('express');
const router = express.Router();
const { runPrediction, runPreprocess, runModelTraining } = require('../controllers/predictionController');

router.post('/predict', runPrediction);
router.post('/preprocess', runPreprocess);
router.post('/train', runModelTraining);

module.exports = router;
