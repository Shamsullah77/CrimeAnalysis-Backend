const Crimes = require("../models/crime");
const { Sequelize, literal, fn, col } = require("sequelize");

// Controller function
exports.analysiseddata = async (req, res) => {
  try {
    // Fetch monthly crime statistics
    const monthlyStats = await Crimes.findAll({
      attributes: [
        [literal("DATE_FORMAT(crimedate, '%b')"), "month"],
        [fn("SUM", col("id")), "totalCrime"],
        [fn("COUNT", col("crimetype")), "totalCrimeType"],
      ],
      group: literal("DATE_FORMAT(crimedate, '%b')"),
    });

    // Fetch unique crime types
    const uniqueCrimeTypes = await Crimes.findAll({
      attributes: [
        [Sequelize.fn("DISTINCT", Sequelize.col("crimetype")), "crimetype"],
      ],
    });

    const crimeTypes = uniqueCrimeTypes.map((crime) =>
      crime.getDataValue("crimetype")
    );

    // Send the response
    res.json({ Status: "Success", monthlyStats, crimeTypes });
  } catch (error) {
    console.error("Error fetching crime data:", error);
    res.status(500).json({ error: "Internal server error" });
  }
};
exports.analysisformdata = async (req, res, next) => {
  try {
    const { crimeType, crimeTime, crimeLocation, guiltyGender } = req.body;

    // Fetch monthly crime statistics with where condition
    const monthlyStatsQuery = Crimes.findAll({
      attributes: [
        [literal("DATE_FORMAT(crimedate, '%b')"), "month"],
        [fn("SUM", col("id")), "totalCrime"],
        [fn("COUNT", col("crimetype")), "totalCrimeType"],
      ],
      where: {
        crimetype: crimeType,
        crimedate: crimeTime,
        crimelocation: crimeLocation,
        guiltygender: guiltyGender,
      },
      group: literal("DATE_FORMAT(crimedate, '%b')"),
    });

    const seacrheddata = await monthlyStatsQuery;
    console.log(seacrheddata);
    res.json({ Status: "Success", seacrheddata });
  } catch (error) {
    console.error("Error fetching analysis data:", error);
    res.status(500).json({ error: "Internal server error" });
  }
};
