const express = require("express");
const cors = require("cors");
const app = express();
const sequelize = require("./Config/db");
const userroutes = require("./routes/userRoutes");
const predictRoute = require('./routes/predictionRoute');
const bodyParser = require('body-parser');





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
.sync()
.then(() => console.log("Database Synced..."))
.catch((err) => console.log("Error: " + err));

// Routes
app.use('/predict', predictRoute);
app.use(userroutes);

app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});