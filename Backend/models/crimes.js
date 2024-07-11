// const { Sequelize, DataTypes } = require("sequelize");
// const sequelize = require("../Config/db");

// const criminal = require("../models/Criminal"); // assuming you haw this table need for primary key of this
// const users = require("../models/users"); // assuming you haw this table need for primary key of this
// const crimetyper = require("../models/crimeType"); // assuming you haw this table need for primary key of this

// const crime = sequelize.define(
//   "crime",
//   {
//     id: {
//       type: DataTypes.INTEGER,
//       autoIncrement: true,
//       primaryKey: true,
//     },
//     Casees: {
//       type: DataTypes.STRING,
//       allowNull: false,
//     },
//     Crimedate: {
//       type: DataTypes.STRING,
//       allowNull: false,
//     },
//     Strategy: {
//       type: DataTypes.STRING,
//       allowNull: false,
     
//     },
//     criminalid: {
//       type: DataTypes.INTEGER,
//       allowNull: false,
//       references: {
//         model: criminal,
//         key: "id",
//       },
//     },

//     crimetypeid: {
//       type: DataTypes.INTEGER,
//       allowNull: false,
//       references: {
//         model: crimetyper,
//         key: "id",
//       },
//     },
//     userid: {
//       type: DataTypes.INTEGER,
//       allowNull: false,
//       references: {
//         model: users,
//         key: "id",
//       },
//     },
//   }
// );
// // relaiton with other tables
// crime.belongsTo(users, { foreignKey: "userid" });
// users.hasMany(crime, { foreignKey: "userid" });

// crime.belongsTo(criminal, { foreignKey: "criminalid" });
// criminal.hasMany(crime, { foreignKey: "criminalid" });

// crime.belongsTo(crimetyper, { foreignKey: "crimetypeid" });
// crimetyper.hasMany(crime, { foreignKey: "crimetypeid" });

// module.exports = crime;




const { Sequelize, DataTypes } = require("sequelize");
const sequelize = require("../Config/db");
const CrimeType = require("./crimeType");

const Crime = sequelize.define("crime", {
  id: {
    type: DataTypes.INTEGER,
    autoIncrement: true,
    primaryKey: true,
  },
  Casees: {
    type: DataTypes.STRING,
    allowNull: false,
  },
  Crimedate: {
    type: DataTypes.STRING,
    allowNull: false,
  },
  Strategy: {
    type: DataTypes.STRING,
    allowNull: false,
  },
  criminalid: {
    type: DataTypes.INTEGER,
    allowNull: false,
  },
  crimetypeid: {
    type: DataTypes.INTEGER,
    allowNull: false,
    references: {
      model: CrimeType,
      key: "id",
    },
  },
  userid: {
    type: DataTypes.INTEGER,
    allowNull: false,
  },
});

Crime.belongsTo(CrimeType, { foreignKey: "crimetypeid" });
CrimeType.hasMany(Crime, { foreignKey: "crimetypeid" });

module.exports = Crime;

