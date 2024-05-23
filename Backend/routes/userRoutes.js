const express = require('express');
const router = express.Router();
const { getusers, createuser , deleteuser} = require('../controllers/userController');

// router.get('/users', getUsers);
// router.post('/addusers', addUser);
// router.delete('/delusers', addUser);


router.post('/createuser', createuser);
router.get('/users', getusers);
router.delete('/deleteuser/:id', deleteuser);





// router.get('/users', getUsers);
// router.post('/addusers', addUser);

module.exports = router;

