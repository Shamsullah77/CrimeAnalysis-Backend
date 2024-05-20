// const db = require('../models/db');

// exports.getUsers = (req, res) => {
//   db.query('SELECT * FROM Users', (err, results) => {
//     if (err) {
//       console.error(err);
//       return res.status(500).json({ message: 'Server error' });
//     }
//     res.json(results);
//   });
// };

// exports.addUser = (req, res) => {
//   const { Name, Email, Password } = req.body;
//   const query = 'INSERT INTO Users (Name, Email, Password) VALUES (?, ?, ?)';
//   db.query(query, [Name, Email, Password], (err, results) => {
//     if (err) {
//       console.error(err);
//       return res.status(500).json({ message: 'Server error' });
//     }
//     res.json({ message: 'User added successfully' });
//   });
// };


const bcrypt = require('bcryptjs');
const User = require('../models/usersModel');

exports.createUser = async (req, res) => {
  try {
    const { Name, Email, Password } = req.body;
    const hashedPassword = await bcrypt.hash(Password, 10);
    const result = await User.create(Name, Email, Password);
    res.status(201).json({ message: 'User created', userId: result.insertId });
  } catch (error) {
    res.status(500).json({ message: 'Server error', error });
  }
};

exports.getUserById = async (req, res) => {
  try {
    const user = await User.findById(req.params.id);
    if (!user) return res.status(404).json({ message: 'User not found' });
    res.status(200).json(user);
  } catch (error) {
    res.status(500).json({ message: 'Server error', error });
  }
};


