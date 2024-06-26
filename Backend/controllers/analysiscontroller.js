const Crimes = require("../models/crimes");
const { Sequelize, literal, fn, col, Op } = require("sequelize");
const CrimeType = require("../models/crimeType");
const Location = require("../models/location");
Crimes.belongsTo(CrimeType, { foreignKey: "crimetypeid", as: "crimetype" });

// Controller function
exports.analysiseddata = async (req, res) => {
  try {
    // Fetch monthly crime statistics
    const monthlyStats = await Crimes.findAll({
      attributes: [
        [literal("DATE_FORMAT(crimedate, '%b')"), "month"],
        [fn("COUNT", col("userid")), "totalCrime"],
        [
          fn("COUNT", fn("DISTINCT", col("crimetype.crimetype"))),
          "totalCrimeType",
        ],
        [fn("COUNT", col("Strategy")), "totalCrimestrategies"],
      ],
      include: [
        {
          model: CrimeType,
          as: "crimetype",
          attributes: [],
        },
      ],
      group: [literal("DATE_FORMAT(crimedate, '%b')")],
    });

    // Fetch unique crime types
    const uniqueCrimeTypes = await CrimeType.findAll({
      attributes: [
        [Sequelize.fn("DISTINCT", Sequelize.col("crimetype")), "crimetype"],
      ],
    });

    const crimeTypes = uniqueCrimeTypes.map((crime) =>
      crime.getDataValue("crimetype")
    );

    console.log(monthlyStats);
    console.log(crimeTypes);

    // Send the response
    res.json({ Status: "Success", monthlyStats, crimeTypes });
  } catch (error) {
    console.error("Error fetching crime data:", error);
    res.status(500).json({ error: "Internal server error" });
  }
};
Crimes.hasMany(Location, { foreignKey: "crimeId", as: "locations" });
exports.analysisformdata = async (req, res, next) => {
  try {
    const { crimeType, crimeTime, crimeLocation } = req.body;
    console.log(crimeTime, crimeType, crimeLocation);
    // Fetch monthly crime statistics with where condition
    const monthlyStatsQuery = Crimes.findAll({
      attributes: [
        [literal("DATE_FORMAT(crimedate, '%b')"), "month"],
        [fn("COUNT", col("userid")), "totalCrime"],
        [
          fn("COUNT", fn("DISTINCT", col("crimetype.crimetype"))),
          "totalCrimeType",
        ],
        [fn("COUNT", col("Strategy")), "totalCrimestrategies"],
      ],
      include: [
        {
          model: CrimeType,
          as: "crimetype",
          attributes: [],
        },
        {
          model: Location,
          as: "locations", // Use the alias defined in the association
          attributes: [],
          where: {
            [Op.or]: [{ Village: crimeLocation }, { District: crimeLocation }],
          },
        },
      ],
      where: {
        crimedate: crimeTime,
      },
      group: [literal("DATE_FORMAT(crimedate, '%b')")],
    });

    const seacrheddata = await monthlyStatsQuery;
    console.log(seacrheddata);
    res.json({ Status: "Success", seacrheddata });
  } catch (error) {
    console.error("Error fetching analysis data:", error);
    res.status(500).json({ error: "Internal server error" });
  }
};
