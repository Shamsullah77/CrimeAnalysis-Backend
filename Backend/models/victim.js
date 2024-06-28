// models/CrimeType.js

const { DataTypes } = require("sequelize");
const sequelize = require("../Config/db"); // Assuming you have a database connection setup
const Criminal = require("../models/Criminal");
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
    criminal: {
      type: DataTypes.INTEGER,
      allowNull: false,
    },
  },
  {
    tableName: "Victim",
  }
);
Victim.belongsTo(Criminal, { foreignKey: "criminal" });
Criminal.hasMany(Victim, { foreignKey: "criminal" });
module.exports = Victim;
