// models/Criminal.js

const { DataTypes } = require("sequelize");
const sequelize = require("../Config/db"); // Assuming you have a database connection setup

const Criminal = sequelize.define(
  "Criminal",
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
    Fname: {
      type: DataTypes.STRING,
      allowNull: false,
    },
    Province: {
      type: DataTypes.STRING,
      allowNull: false,
    },
    Dob: {
      type: DataTypes.DATE,
      allowNull: false,
    },
    Experience: {
      type: DataTypes.STRING,
      allowNull: false,
    },
    Economical_situation: {
      type: DataTypes.STRING,
      allowNull: false,
    },
    Education_level: {
      type: DataTypes.STRING,
      allowNull: false,
    },
    Phone: {
      type: DataTypes.STRING,
      allowNull: false,
    },
    Ssn: {
      type: DataTypes.STRING,
      allowNull: false,
    },
    Gender: {
      type: DataTypes.BOOLEAN,
      allowNull: false,
    },
    Image: {
      type: DataTypes.BLOB,
      allowNull: true,
    },
  },
  {
    tableName: "Criminal",
    timestamps: false,
  }
);

module.exports = Criminal;
