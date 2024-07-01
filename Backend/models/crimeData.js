// Backend/models/data.js

const { DataTypes } = require('sequelize');
const sequelize = require('../Config/db'); // Adjust the path based on your actual setup

const Data = sequelize.define('crimeData', {
  date: {
    type: DataTypes.DATE,
    allowNull: false,
  },
  hour_of_day: {
    type: DataTypes.INTEGER,
    allowNull: false,
  },
  location: {
    type: DataTypes.STRING,
    allowNull: false,
  },
  victim_gender: {
    type: DataTypes.STRING,
    allowNull: false,
  },
  victim_age: {
    type: DataTypes.INTEGER,
    allowNull: false,
  },
  perpetrator_gender: {
    type: DataTypes.STRING,
    allowNull: false,
  },
  perpetrator_age: {
    type: DataTypes.INTEGER,
    allowNull: false,
  },
  weapon: {
    type: DataTypes.STRING,
    allowNull: false,
  },
  injury: {
    type: DataTypes.STRING,
    allowNull: false,
  },
  weather: {
    type: DataTypes.STRING,
    allowNull: false,
  },
  temperature: {
    type: DataTypes.FLOAT,
    allowNull: false,
  },
  previous_activity: {
    type: DataTypes.STRING,
    allowNull: false,
  },
  economical_situation: {
    type: DataTypes.STRING,
    allowNull: false,
  },
  education_level: {
    type: DataTypes.STRING,
    allowNull: false,
  },
  crime_type: {
    type: DataTypes.STRING,
    allowNull: false,
  },
  time_of_day: {
    type: DataTypes.STRING,
    allowNull: false,
  },
  day_of_week: {
    type: DataTypes.STRING,
    allowNull: false,
  },
  month: {
    type: DataTypes.STRING,
    allowNull: false,
  },
  season: {
    type: DataTypes.STRING,
    allowNull: false,
  },
  victim_age_group: {
    type: DataTypes.STRING,
    allowNull: false,
  },
  perpetrator_age_group: {
    type: DataTypes.STRING,
    allowNull: false,
  },
  weather_condition: {
    type: DataTypes.STRING,
    allowNull: false,
  },
  economic_index: {
    type: DataTypes.FLOAT,
    allowNull: false,
  },
  education_index: {
    type: DataTypes.FLOAT,
    allowNull: false,
  },
}, {
  timestamps: false,
});

module.exports =Data ;
