// models/Address.js
const { DataTypes } = require("sequelize");
const sequelize = require("../Config/db");
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
    Temperature: {
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

    // Ensure the column name matches existing database schema
    crimeId: {
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

// Define the relationship between tables
Location.belongsTo(Crime, { foreignKey: "crimeId" });
Crime.hasMany(Location, { foreignKey: "crimeId" });

module.exports = Location;
