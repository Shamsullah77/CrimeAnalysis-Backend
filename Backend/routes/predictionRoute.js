const express = require('express');
const router = express.Router();
const { runPrediction } = require('../controllers/predictionController');

router.post('/', runPrediction);

module.exports = router;
