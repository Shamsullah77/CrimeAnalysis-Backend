// const { Sequelize, DataTypes } = require('sequelize');
// const sequelize = require('../Config/db');

// const User = sequelize.define('users', {
//     name: {
//         type: DataTypes.STRING,
//         allowNull: false
//     },
//     email: {
//         type: DataTypes.STRING,
//         allowNull: false,
//         unique: true
//     },
//     password: {
//         type: DataTypes.STRING,
//         allowNull: false
//     }
// }, {timestamps: false
    
// });
// console.log('database is connected');
// module.exports = User
const { Sequelize, DataTypes } = require('sequelize');
const sequelize = require('../Config/db');

const User = sequelize.define('users', {
  name: {
    type: DataTypes.STRING,
    allowNull: false
  },
  email: {
    type: DataTypes.STRING,
    allowNull: false,
    unique: true
  },
  password: {
    type: DataTypes.STRING,
    allowNull: false
  }
}, { timestamps: false });

module.exports = User;
