// models/CrimeType.js

const { DataTypes } = require("sequelize");
const sequelize = require("../Config/db"); // Assuming you have a database connection setup

const Victim = sequelize.define(
  "Victim",
  {
    id: {
      type: DataTypes.INTEGER,
      primaryKey: true,
      autoIncrement: true,
    },
    Name: {
      type: DataTypes.STRING,
      allowNull: false,
    },
    Lname: {
      type: DataTypes.STRING,
      allowNull: false,
    },
    Province: {
      type: DataTypes.STRING,
      allowNull: false,
    },
    Age: {
      type: DataTypes.INTEGER,
      allowNull: false,
    },
    Gender: {
      type: DataTypes.STRING,
      allowNull: false,
    },
  },
  {
    tableName: "Victim",
  }
);

module.exports = Victim;
