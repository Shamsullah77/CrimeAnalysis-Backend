// Backend/loadData.js

const fs = require('fs');
const csv = require('csv-parser');
const sequelize = require('../Config/db');
const Data = require('../models/crimeData');

const results = [];

fs.createReadStream('../AiModel/data.csv')
  .pipe(csv())
  .on('data', (data) => results.push(data))
  .on('end', () => {
    sequelize.sync()
      .then(() => {
        return Data.bulkCreate(results, { validate: true });
      })
      .then(() => {
        console.log('Data loaded successfully');
      })
      .catch((error) => {
        console.error('Error loading data:', error);
      });
  });
