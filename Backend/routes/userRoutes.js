
const express = require('express');
const router = express.Router();
const { getusers, createuser, deleteuser } = require('../controllers/userController');

router.post('/createuser', createuser);
router.get('/users', getusers);
router.delete('/deleteuser/:id', deleteuser);

module.exports = router;




