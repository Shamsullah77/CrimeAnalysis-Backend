const express = require('express');
const router = express.Router();
const { runPrediction } = require('../controllers/predictionController');

router.post('/predict', runPrediction);

module.exports = router;
