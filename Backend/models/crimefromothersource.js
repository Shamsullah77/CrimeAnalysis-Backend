const { DataTypes } = require("sequelize");
const sequelize = require("../Config/db"); // Assuming you have a database connection setup

const crimefromothersource = sequelize.define(
  "crimefromothersource",
  {
    id: {
      type: DataTypes.INTEGER,
      primaryKey: true,
      autoIncrement: true,
    },
    Criminal_name: {
      type: DataTypes.STRING,
      allowNull: false,
    },
    Crime_type: {
      type: DataTypes.STRING,
      allowNull: false,
    },
    Crime_date: {
      type: DataTypes.DATE,
      allowNull: false,
    },
    Hour_of_day: {
      type: DataTypes.TIME,
      allowNull: false,
    },
    Location: {
      type: DataTypes.STRING,
      allowNull: false,
    },
    Victim_gender: {
      type: DataTypes.STRING,
      allowNull: false,
    },
    Perpetrator_gender: {
      type: DataTypes.STRING,
      allowNull: false,
    },
    Perpetrator_age: {
      type: DataTypes.INTEGER,
      allowNull: false,
    },
    Weapon: {
      type: DataTypes.STRING,
      allowNull: false,
    },
    Injury: {
      type: DataTypes.STRING,
      allowNull: false,
    },
    Weather: {
      type: DataTypes.STRING,
      allowNull: false,
    },
    Temperature: {
      type: DataTypes.INTEGER,
      allowNull: false,
    },
    Previous_activity: {
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
  },
  {
    tableName: "crimefromothersource",
    timestamps: false,
  }
);

module.exports = crimefromothersource;
