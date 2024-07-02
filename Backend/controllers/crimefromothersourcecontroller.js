const crimefromothersource = require("../models/crimefromothersource");
const upload = require("../middleware/upload");

const fs = require("fs");
const path = require("path");

// Function to get all crime data from other sources
exports.getCrimeFromOtherSourcedata = async (req, res) => {
  try {
    const crimes = await crimefromothersource.findAll(); // Assuming you're using Sequelize
    console.log(crimes);
    res.status(201).json({ Status: "Success", crimes });
  } catch (error) {
    console.error("Error retrieving crime data:", error);
    res
      .status(500)
      .json({ Status: "Error", message: "Could not retrieve data" });
  }
};

// Function to delete a crime record by ID
exports.deleteCrimeById = async (req, res) => {
  const { id } = req.params;

  try {
    const result = await crimefromothersource.destroy({ where: { id } });

    if (result) {
      res
        .status(200)
        .json({ Status: "Success", message: "Record deleted successfully" });
    } else {
      res.status(404).json({ Status: "Error", message: "Record not found" });
    }
  } catch (error) {
    console.error("Error deleting record:", error);
    res
      .status(500)
      .json({ Status: "Error", message: "Could not delete record" });
  }
};

exports.saveDataToJson = async (req, res) => {
  try {
    const newCrimes = await crimefromothersource.findAll();

    const jsonFilePath = path.join(__dirname, "..", "data", "crimesData.json");
    let existingCrimes = [];

    // Check if the file exists and read the existing data
    if (fs.existsSync(jsonFilePath)) {
      const data = fs.readFileSync(jsonFilePath, "utf-8");
      existingCrimes = JSON.parse(data);
    }

    // Combine the existing data with the new data
    const combinedCrimes = existingCrimes.concat(newCrimes);

    // Write the combined data back to the JSON file
    fs.writeFileSync(
      jsonFilePath,
      JSON.stringify(combinedCrimes, null, 2),
      "utf-8"
    );

    res
      .status(200)
      .json({ Status: "Success", message: "Data saved to JSON file" });
  } catch (error) {
    console.error("Error saving data to JSON file:", error);
    res.status(500).json({ Status: "Error", message: "Could not save data" });
  }
};

exports.getcrimefromothesource = (req, res) => {
  upload(req, res, async (err) => {
    if (err) {
      return res.status(400).json({ Status: "Error", message: err });
    }

    const {
      criminla_name,
      crime_type,
      crime_date,
      hour_of_day,
      location,
      victim_gender,
      perpetrator_gender,
      Perpetrator_age,
      weapon,
      injury,
      weather,
      temperature,
      previous_activity,
      economical_situation,
      education_level,
    } = req.body;

    // Image data from multer
    // const image = req.file ? req.file.buffer : null;

    try {
      const newCriminal = await crimefromothersource.create({
        Criminal_name: criminla_name,
        Crime_type: crime_type,
        Crime_date: crime_date,
        Hour_of_day: hour_of_day,
        Location: location,
        Victim_gender: victim_gender,
        Perpetrator_age: Perpetrator_age,
        Perpetrator_gender: perpetrator_gender,
        Weapon: weapon,
        Injury: injury,
        Weather: weather,
        Temperature: temperature,
        Previous_activity: previous_activity,
        Economical_situation: economical_situation,
        Education_level: education_level,
      });

      res.status(201).json({ Status: "Success" });
    } catch (error) {
      console.error("Error saving criminal data:", error);
      res.status(500).json({ Status: "Error", message: "Could not save data" });
    }
  });
};
