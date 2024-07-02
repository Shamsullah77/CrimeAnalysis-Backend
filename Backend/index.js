const express = require("express");
const cors = require("cors");
const app = express();
const { FORCE } = require("sequelize/lib/index-hints");
const { PythonShell } = require("python-shell");
const sequelize = require("./Config/db");
const User = require("./models/users");
const location = require("./models/location");
const Criminal = require("./models/Criminal");
const Victim = require("./models/victim");
const CrimeType = require("./models/crimeType");
const Crimes = require("./models/crimes");
const userfeedback = require("./models/userfeedback");
const predictRoute = require("./routes/predictionRoute");
const userroutes = require("./routes/userRoutes");

const PORT = process.env.PORT || 3002;

// Middleware
app.use(cors());
app.use(express.json());
require("dotenv").config();
app.use(userroutes);
app.use("/predict", predictRoute);

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
