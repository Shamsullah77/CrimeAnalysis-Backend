const { Sequelize } = require("sequelize");

const sequelize = new Sequelize("cap", "root", "", {
  host: "localhost",
  dialect: "mysql",
  database: "cap",
  password: "",
});

module.exports = sequelize;
