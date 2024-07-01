// Backend/controllers/dataController.js

const fs = require('fs');
const csv = require('csv-parser');
const sequelize = require('../Config/db');
const Data = require('../models/crimeData');

exports.loadData = async (req, res) => {
  const results = [];

  fs.createReadStream('../../AiModel/data.csv') // Adjust the path based on your setup
    .pipe(csv())
    .on('data', (data) => results.push(data))
    .on('end', async () => {
      try {
        await sequelize.sync();
        await Data.bulkCreate(results, { validate: true });
        res.status(200).json({ message: 'Data loaded successfully' });
      } catch (error) {
        console.error('Error loading data:', error);
        res.status(500).json({ message: 'Error loading data', error });
      }
    });
};
