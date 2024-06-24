const express = require("express");
const cors = require("cors");
const app = express();
const sequelize = require("./Config/db");
const User = require("./models/users");
//const Crime = require("./models/crime");
const userroutes = require("./routes/userRoutes");
// Middleware
app.use(cors());
app.use(express.json());
require("dotenv").config();
const PORT = process.env.PORT || 3002;
app.use(userroutes);

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
