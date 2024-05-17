const express = require('express');
const router = express.Router();
const { addAnalysis } = require('../controllers/userLavelController');

router.post('/adduserLavel', addAnalysis);

module.exports = router;
