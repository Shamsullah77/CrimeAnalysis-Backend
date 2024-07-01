// Backend/util/dataLoader.js
const fs = require('fs');
const path = require('path');
const { Sequelize, DataTypes, Op } = require('sequelize');
const csvWriter = require('csv-writer').createObjectCsvWriter;

const sequelize = new Sequelize('database', 'username', 'password', {
  database:'cap1',
  host: 'localhost',
  dialect: 'mysql',
});

const CrimeData = sequelize.define('CrimeData', {
  date: { type: DataTypes.DATE, allowNull: false },
  hour_of_day: { type: DataTypes.INTEGER, allowNull: false },
  location: { type: DataTypes.STRING, allowNull: false },
  victim_gender: { type: DataTypes.STRING, allowNull: false },
  victim_age: { type: DataTypes.INTEGER, allowNull: false },
  perpetrator_gender: { type: DataTypes.STRING, allowNull: false },
  perpetrator_age: { type: DataTypes.INTEGER, allowNull: false },
  weapon: { type: DataTypes.STRING, allowNull: false },
  injury: { type: DataTypes.STRING, allowNull: false },
  weather: { type: DataTypes.STRING, allowNull: false },
  temperature: { type: DataTypes.FLOAT, allowNull: false },
  previous_activity: { type: DataTypes.STRING, allowNull: false },
  economical_situation: { type: DataTypes.STRING, allowNull: false },
  education_level: { type: DataTypes.STRING, allowNull: false },
  crime_type: { type: DataTypes.STRING, allowNull: false },
  time_of_day: { type: DataTypes.STRING, allowNull: false },
  day_of_week: { type: DataTypes.STRING, allowNull: false },
  month: { type: DataTypes.STRING, allowNull: false },
  season: { type: DataTypes.STRING, allowNull: false },
  victim_age_group: { type: DataTypes.STRING, allowNull: false },
  perpetrator_age_group: { type: DataTypes.STRING, allowNull: false },
  weather_condition: { type: DataTypes.STRING, allowNull: false },
  economic_index: { type: DataTypes.FLOAT, allowNull: false },
  education_index: { type: DataTypes.FLOAT, allowNull: false },
}, {
  tableName: 'crimedata',
  timestamps: false,
});

const getLastProcessedDate = () => {
  try {
    return fs.readFileSync(path.join(__dirname, 'lastProcessedDate.txt'), 'utf8');
  } catch (err) {
    return null;
  }
};

const saveLastProcessedDate = (date) => {
  fs.writeFileSync(path.join(__dirname, 'lastProcessedDate.txt'), date, 'utf8');
};

const loadDataToCsv = async () => {
  const lastProcessedDate = getLastProcessedDate();
  const whereCondition = lastProcessedDate ? { date: { [Op.gt]: new Date(lastProcessedDate) } } : {};

  console.log(`Fetching data with condition: ${JSON.stringify(whereCondition)}`);

  try {
    const data = await CrimeData.findAll({
      where: whereCondition,
      raw: true,
    });

    console.log(`Fetched ${data.length} records from the database`);

    if (data.length > 0) {
      const csvPath = path.join(__dirname, '../../AiModel/data.csv');
      const writer = csvWriter({
        path: csvPath,
        header: [
          { id: 'date', title: 'Date' },
          { id: 'hour_of_day', title: 'Hour of Day' },
          { id: 'location', title: 'Location' },
          { id: 'victim_gender', title: 'Victim Gender' },
          { id: 'victim_age', title: 'Victim Age' },
          { id: 'perpetrator_gender', title: 'Perpetrator Gender' },
          { id: 'perpetrator_age', title: 'Perpetrator Age' },
          { id: 'weapon', title: 'Weapon' },
          { id: 'injury', title: 'Injury' },
          { id: 'weather', title: 'Weather' },
          { id: 'temperature', title: 'Temperature' },
          { id: 'previous_activity', title: 'Previous Activity' },
          { id: 'economical_situation', title: 'Economical Situation' },
          { id: 'education_level', title: 'Education Level' },
          { id: 'crime_type', title: 'Crime Type' },
          { id: 'time_of_day', title: 'Time of Day' },
          { id: 'day_of_week', title: 'Day of Week' },
          { id: 'month', title: 'Month' },
          { id: 'season', title: 'Season' },
          { id: 'victim_age_group', title: 'Victim Age Group' },
          { id: 'perpetrator_age_group', title: 'Perpetrator Age Group' },
          { id: 'weather_condition', title: 'Weather Condition' },
          { id: 'economic_index', title: 'Economic Index' },
          { id: 'education_index', title: 'Education Index' },
        ],
      });

      await writer.writeRecords(data);
      console.log('Data written to CSV file');

      const lastDate = data[data.length - 1].date;
      saveLastProcessedDate(lastDate.toISOString());
      console.log(`Last processed date saved: ${lastDate.toISOString()}`);
    } else {
      console.log('No new data to process');
    }
  } catch (error) {
    console.error('Error fetching or writing data:', error);
  }
};

const runService = () => {
  loadDataToCsv()
    .then(() => {
      console.log('Data loaded successfully');
    })
    .catch(err => {
      console.error('Error loading data:', err);
    });
};

setInterval(runService, 5000);
