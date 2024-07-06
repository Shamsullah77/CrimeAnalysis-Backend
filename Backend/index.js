const express = require("express");
const cors = require("cors");
const app = express();
const sequelize = require("./Config/db");
const predictionRoutes = require('./routes/predictionRoute');
const userroutes = require("./routes/userRoutes");

const PORT = process.env.PORT || 3002;

// Middleware
app.use(cors());
app.use(express.json());
require("dotenv").config();
app.use(userroutes);
app.use("/api", predictionRoutes);  // Update this line to handle all prediction routes under /api

// Test database connection
sequelize
  .authenticate()
  .then(() => console.log("Database connected..."))
  .catch((err) => console.log("Error: " + err));

// Sync database
sequelize
  .sync()
  .then(() => console.log("Database Connected..."))
  .catch((err) => console.log("Error: " + err));

app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
