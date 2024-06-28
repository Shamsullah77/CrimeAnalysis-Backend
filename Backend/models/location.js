// models/Address.js
const { DataTypes } = require("sequelize");
const sequelize = require("../Config/db");
const Criminal = require("./Criminal"); // Assuming you have a Criminal model
const Crime = require("./crimes"); // Assuming you have a Crime model

const Location = sequelize.define(
  "Location",
  {
    id: {
      type: DataTypes.INTEGER,
      primaryKey: true,
      autoIncrement: true,
    },
    province: {
      type: DataTypes.STRING,
      allowNull: false,
    },
    District: {
      type: DataTypes.STRING,
      allowNull: false,
    },
    Village: {
      type: DataTypes.STRING,
      allowNull: false,
    },
    Weather: {
      type: DataTypes.STRING,
      allowNull: false,
    },
    Temprature: {
      type: DataTypes.STRING,
      allowNull: false,
    },
    Latitude: {
      type: DataTypes.STRING,
      allowNull: false,
    },
    Longitude: {
      type: DataTypes.STRING,
      allowNull: false,
    },
    Areaimage: {
      type: DataTypes.STRING,
      allowNull: false,
    },
    crimeid: {
      type: DataTypes.INTEGER,
      allowNull: false,
      references: {
        model: Crime,
        key: "id",
      },
    },
  },
  {
    tableName: "Location",
  }
);

// defining the realation between tables

Location.belongsTo(Crime, { foreignKey: "crimeid" });
Crime.hasMany(Location, { foreignKey: "crimeid" });

module.exports = Location;
