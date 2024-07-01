const express = require("express");
const cors = require("cors");
const app = express();
const sequelize = require("./Config/db");
const User = require("./models/users");
const Criminal = require("./models/Criminal");
const location = require("./models/location");
const Victim = require("./models/victim");
const CrimeType = require("./models/crimeType");
const Crimes = require("./models/crimes");
const userfeedback = require("./models/userfeedback");

const userroutes = require("./routes/userRoutes");
const bodyParser = require("body-parser");
const { PythonShell } = require("python-shell");

const predictRoute = require("./routes/predictionRoute");

// Other middleware and routes

app.use("/predict", predictRoute);

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
