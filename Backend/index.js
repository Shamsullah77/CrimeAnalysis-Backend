

const express = require('express');
const cors = require('cors');
const app = express();
require('dotenv').config();
const userRoutes = require('./routes/userRoutes');
const sequelize = require('./Config/db');

// Middleware
app.use(cors());
app.use(express.json());

// Routes
app.use('/api', userRoutes);

// Test database connection
sequelize.authenticate()
  .then(() => console.log('Database connected...'))
  .catch(err => console.log('Error: ' + err));

// Sync database
sequelize.sync()
  .then(() => console.log('Database Connected...'))
  .catch(err => console.log('Error: ' + err));

const PORT = process.env.PORT || 3002;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});



