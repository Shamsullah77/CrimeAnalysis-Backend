
const { Sequelize } = require('sequelize');

const sequelize = new Sequelize('caps', 'root', '', {
  host: 'localhost',
  dialect: 'mysql',
  database: 'caps',
  password: '',
});

module.exports = sequelize;
