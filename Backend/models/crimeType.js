// // models/CrimeType.js

// const { DataTypes } = require("sequelize");
// const sequelize = require("../Config/db"); // Assuming you have a database connection setup

// const CrimeType = sequelize.define("Crimetype", {
//   id: {
//     type: DataTypes.INTEGER,
//     primaryKey: true,
//     autoIncrement: true,
//   },
//   Crimetype: {
//     type: DataTypes.STRING,
//     allowNull: false,
//   },
// });
// module.exports = CrimeType;


const { Sequelize, DataTypes } = require("sequelize");
const sequelize = require("../Config/db");

const CrimeType = sequelize.define("crimeType", {
  id: {
    type: DataTypes.INTEGER,
    autoIncrement: true,
    primaryKey: true,
  },
  Crimetype: {
    type: DataTypes.STRING,
    allowNull: false,
  },
});

module.exports = CrimeType;
