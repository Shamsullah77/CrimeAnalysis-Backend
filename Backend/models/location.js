const { DataTypes } = require("sequelize");
const sequelize = require("../Config/db");
const Crime = require("./crimes"); // Assuming you have a Crime model

const Location = sequelize.define("Area", {
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
  cid: {
    type: DataTypes.INTEGER,
    allowNull: false,
    references: {
      model: Crime,
      key: "id",
    },
  },
});
// Defining the relation between tables
Location.belongsTo(Crime, { foreignKey: "cid" });
Crime.hasMany(Location, { foreignKey: "cid" });

module.exports = Location;
