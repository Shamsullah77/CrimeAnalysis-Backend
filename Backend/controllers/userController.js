const db = require('../Config/db');
const User = require('../models/users');

exports.getUsers = (req, res) => {
  db.query('SELECT * FROM Users', (err, results) => {
    if (err) {
      console.error(err);
      return res.status(500).json({ message: 'Server error' });
    }
    res.json(results);
  });
};

exports.addUser = (req, res) => {
  const { Name, Email, Password } = req.body;
  const query = 'INSERT INTO Users (Name, Email, Password)  VALUES ("sahil", "sahil@gmail.com", "sahil123")';
  db.query(query, [Name, Email, Password], (err, results) => {
    if (err) {
      console.error(err);
      return res.status(500).json({ message: 'Server error' });
    }
    res.json({ message: 'User added successfully' });
  });
};



exports.getusers = async (req, res) => {
  try {
    const users = await User.findAll();
    res.status(200).json(users);
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
};



exports.createuser = async (req, res) => {
  const { name, email, password } = req.body;

  try {
    const newUser = await User.create({
      name: 'samim',
      email: 'sahil@gmail.com',
      password: 'samimkhan'
    });

    res.status(201).json(newUser);
  } catch (err) {
    res.status(400).json({ message: err.message });
  }
};




exports.deleteuser = async (req, res) => {
  try {
    const user = await User.findByPk(req.params.id);
    if (!user) {
      return res.status(404).json({ message: 'User not found' });
    }

    await user.destroy();
    res.status(200).json({ message: 'User deleted successfully' });
  } catch (err) {
    res.status(500).json({ message: err.message });
  }
};