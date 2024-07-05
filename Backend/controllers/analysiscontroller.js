const Crimes = require("../models/crimes");
const { Sequelize, literal, fn, col, Op } = require("sequelize");
const CrimeType = require("../models/crimeType");
const Location = require("../models/location");

// Define associations
Crimes.belongsTo(CrimeType, { foreignKey: "crimetypeid", as: "crimetype" });
Crimes.hasMany(Location, { foreignKey: "crimeId", as: "locations" });

exports.analysiseddata = async (req, res) => {
  try {
    // Fetch monthly crime statistics

    const monthlyStatsQuery = await Crimes.findAll({
      attributes: [
        "id",
        [literal("DATE_FORMAT(Crimedate, '%Y-%m')"), "Month"],
        [fn("COUNT", fn("DISTINCT", col("crimetype.id"))), "CrimetypesCount"],
        [
          fn("COUNT", fn("DISTINCT", col("Crime.criminalId"))),
          "CriminalsCount",
        ],
        [fn("COUNT", fn("DISTINCT", col("Crime.id"))), "CrimesCount"],
      ],
      include: [
        {
          model: CrimeType,
          as: "crimetype",
          attributes: [],
        },
        {
          model: Location,
          as: "locations",
          attributes: [],
          required: false, // To simulate LEFT OUTER JOIN
        },
      ],

      group: [literal("DATE_FORMAT(Crimedate, '%Y-%m')")],
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
    // analysis according to days

    const results = await Crimes.findAll({
      attributes: [
        [fn("DAYNAME", col("Crimedate")), "day"],
        [fn("COUNT", col("id")), "count"],
      ],
      group: [literal("day")],
    });

    const daysOfWeek = [
      "Sunday",
      "Monday",
      "Tuesday",
      "Wednesday",
      "Thursday",
      "Friday",
      "Saturday",
    ];
    const formattedResults = daysOfWeek.map((day) => {
      const found = results.find((result) => result.dataValues.day === day);
      return { day, count: found ? found.dataValues.count : 0 };
    });

    console.log(formattedResults);
    // console.log(monthlyStatsQuery);
    // console.log(crimeTypes);

    // Send the response
    res.json({
      Status: "Success",
      monthlyStats: monthlyStatsQuery,
      crimeTypes,
      daysdata: formattedResults,
    });
  } catch (error) {
    console.error("Error fetching crime data:", error);
    res.status(500).json({ error: "Internal server error" });
  }
};

exports.analysisformdata = async (req, res, next) => {
  try {
    const { crimeType, crimeTime, crimeLocation } = req.body;
    console.log(crimeTime, crimeType, crimeLocation);

    const monthlyStatsQuery = await Crimes.findAll({
      attributes: [
        "id",
        [literal("DATE_FORMAT(Crimedate, '%Y-%m')"), "Month"],
        [fn("COUNT", fn("DISTINCT", col("crimetype.id"))), "CrimetypesCount"],
        [
          fn("COUNT", fn("DISTINCT", col("Crime.criminalId"))),
          "CriminalsCount",
        ],
        [fn("COUNT", fn("DISTINCT", col("Crime.id"))), "CrimesCount"],
      ],
      include: [
        {
          model: CrimeType,
          as: "crimetype",
          attributes: [],
        },
        {
          model: Location,
          as: "locations",
          attributes: [],
          required: false, // To simulate LEFT OUTER JOIN
        },
      ],
      where: {
        [Op.or]: [
          { "$crimetype.Crimetype$": crimeType },
          { "$locations.District$": crimeLocation },
          Sequelize.where(
            fn("YEAR", col("Crimedate")),
            fn("YEAR", literal(crimeTime))
          ),
        ],
      },
      group: [literal("DATE_FORMAT(Crimedate, '%Y-%m')")],
    });

    console.log(monthlyStatsQuery);
    res.json({ Status: "Success", seacrheddata: monthlyStatsQuery });
  } catch (error) {
    console.error("Error fetching analysis data:", error);
    res.status(500).json({ error: "Internal server error" });
  }
};

//data for graphs for each daya sunday........
