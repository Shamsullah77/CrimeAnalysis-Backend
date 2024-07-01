const { DataTypes } = require("sequelize");
const sequelize = require("../Config/db"); // adjust the path as needed
const User = require("../models/users");
const Feedback = sequelize.define(
  "Feedback",
  {
    feedbackId: {
      type: DataTypes.INTEGER,
      autoIncrement: true,
      primaryKey: true,
    },
    userId: {
      type: DataTypes.INTEGER,
      allowNull: false,
    },
    feedback: {
      type: DataTypes.TEXT,
      allowNull: false,
    },
  },
  {
    tableName: "feedbacks", // optional: specify a custom table name
    timestamps: true, // optional: automatically adds createdAt and updatedAt fields
  }
);
// Define the association
Feedback.belongsTo(User, { foreignKey: "userId" });
User.hasMany(Feedback, { foreignKey: "userId" });
module.exports = Feedback;
