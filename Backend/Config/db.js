const { Sequelize } = require("sequelize");

const sequelize = new Sequelize("cap1", "root", "", {
  host: "localhost",
  dialect: "mysql",
  database: "cap1",
  password: "",
});

module.exports = sequelize;
