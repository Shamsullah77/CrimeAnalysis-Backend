const { DataTypes } = require("sequelize");
const sequelize = require("../Config/db");
const bcrypt = require("bcryptjs");

const User = sequelize.define(
  "User",
  {
    Name: {
      type: DataTypes.STRING,
      allowNull: false,
    },
    Email: {
      type: DataTypes.STRING,
      allowNull: false,
      unique: {
        msg: "Email address is already in use",
      },
      validate: {
        isEmail: true,
      },
    },
    Password: {
      type: DataTypes.STRING,
      allowNull: false,
    },
    role: {
      type: DataTypes.STRING,
      enum: ["user", "admin"],
      defaultValue: "user",
    },
  },
  {
    hooks: {
      beforeCreate: async (user) => {
        if (user.Password) {
          const salt = await bcrypt.genSalt(10);
          user.Password = await bcrypt.hash(user.Password, salt);
        }
      },
    },
  }
);

module.exports = User;
