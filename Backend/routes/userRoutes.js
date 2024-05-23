// const express = require('express');
// const router = express.Router();
// const { getUsers, addUser } = require('../controllers/userController');

// router.get('/users', getUsers);
// router.post('/addusers', addUser);

// module.exports = router;

const express = require('express');
const router = express.Router();
const { getusers, createuser , deleteuser} = require('../controllers/userController');

// router.get('/users', getUsers);
// router.post('/addusers', addUser);
// router.delete('/delusers', addUser);

// changes by sahil
router.post('/createuser', createuser);
router.get('/users', getusers);
router.delete('/deleteuser/:id', deleteuser);





// router.get('/users', getUsers);
// router.post('/addusers', addUser);
const userController = require('../controllers/userController');

// POST /api/users to create a new user
router.post('/users', userController.createUser);

// GET /api/users/:id to get a user by ID
router.get('/users/:id', userController.getUserById);

module.exports = router;


