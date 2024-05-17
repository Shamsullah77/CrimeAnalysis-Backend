const express = require('express');
const router = express.Router();
const { getUsers, addUser } = require('../controllers/userController');

router.get('/users', getUsers);
router.post('/addusers', addUser);

module.exports = router;

