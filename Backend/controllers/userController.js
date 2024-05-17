const db = require('../models/db');

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
  const query = 'INSERT INTO Users (Name, Email, Password) VALUES (?, ?, ?)';
  db.query(query, [Name, Email, Password], (err, results) => {
    if (err) {
      console.error(err);
      return res.status(500).json({ message: 'Server error' });
    }
    res.json({ message: 'User added successfully' });
  });
};
