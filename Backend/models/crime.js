const { DataTypes } = require("sequelize");
const sequelize = require("../Config/db");
const bcrypt = require("bcryptjs");

const Crime = sequelize.define("Crimeeee", {
  crimetype: {
    type: DataTypes.STRING,
    allowNull: false,
  },
  crimedate: {
    type: DataTypes.DATEONLY,
    allowNull: false,
  },
  crimelocation: {
    type: DataTypes.STRING,
    allowNull: false,
  },
  guiltyname: {
    type: DataTypes.STRING,
    allowNull: false,
  },
  guiltygender: {
    type: DataTypes.STRING,
    allowNull: false,
  },
  guiltyssn: {
    type: DataTypes.STRING,
    allowNull: false,
  },
  guiltyprovince: {
    type: DataTypes.STRING,
    allowNull: false,
  },
  giultyphone: {
    type: DataTypes.STRING,
    allowNull: false,
  },
  evidence: {
    type: DataTypes.STRING,
    allowNull: false,
  },
  areaoffice: {
    type: DataTypes.STRING,
    allowNull: false,
  },
  crimehardness: {
    type: DataTypes.STRING,
    allowNull: false,
  },
  crimeremark: {
    type: DataTypes.STRING,
    allowNull: false,
  },
  criminalameg: {
    type: DataTypes.BLOB,
    allowNull: false,
  },
  guiltyimage: {
    type: DataTypes.BLOB,
    allowNull: false,
  },
});

module.exports = Crime;
