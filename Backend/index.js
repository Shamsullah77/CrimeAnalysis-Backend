const express = require("express");
const cors = require("cors");
const app = express();
const sequelize = require("./Config/db");
<<<<<<< HEAD
const userroutes = require("./routes/userRoutes");
const predictRoute = require('./routes/predictionRoute');
const bodyParser = require('body-parser');

=======
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
>>>>>>> b1bd8cde73001684658800a2a3979c240463e67b


<<<<<<< HEAD

=======
app.use("/predict", predictRoute);
>>>>>>> b1bd8cde73001684658800a2a3979c240463e67b

app.use(cors());
app.use(express.json());
app.use(bodyParser.json());
require("dotenv").config();
const PORT = process.env.PORT || 3002;

// Test database connection
sequelize
.authenticate()
.then(() => console.log("Database connected..."))
.catch((err) => console.log("Error: " + err));

// Sync database
sequelize
<<<<<<< HEAD
.sync()
.then(() => console.log("Database Synced..."))
.catch((err) => console.log("Error: " + err));

// Routes
app.use('/predict', predictRoute);
app.use(userroutes);

app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
=======
  .sync()
  .then(() => console.log("Database Connected..."))
  .catch((err) => console.log("Error: " + err));

app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
>>>>>>> b1bd8cde73001684658800a2a3979c240463e67b
