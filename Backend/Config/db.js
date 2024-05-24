// const mysql = require('mysql2');

// const connection = mysql.createConnection({
//   host: 'localhost',
//   user: 'root',
//   password: '',
//   database: 'caps',
// });

// connection.connect((err) => {
//   if (err) throw err;
//   console.log('Connected to MySQL');
// });

// module.exports = connection;

const { Sequelize } = require('sequelize');

const sequelize = new Sequelize('caps', 'root', '', {
  host: 'localhost',
  dialect: 'mysql'
});



module.exports = sequelize;
