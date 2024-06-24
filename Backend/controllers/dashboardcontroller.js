const Crimes = require("../models/crime");
const { literal, fn, col } = require("sequelize");

exports.dashboard = async (req, res) => {
  try {
    // Count distinct values
    const distinctCounts = await Crimes.findAll({
      attributes: [
        [fn("COUNT", fn("DISTINCT", col("crimetype"))), "distinctCrimeType"],
        [
          fn("COUNT", fn("DISTINCT", col("crimelocation"))),
          "distinctCrimeLocation",
        ],
        [fn("COUNT", fn("DISTINCT", col("evidence"))), "distinctCrimeEvidence"],
      ],
    });

    // Fetch total count of all crimes
    const totalCrime = await Crimes.count();

    // Access individual counts
    const distinctCrimeType = distinctCounts[0].get("distinctCrimeType");
    const distinctCrimeLocation = distinctCounts[0].get(
      "distinctCrimeLocation"
    );
    const distinctCrimeEvidence = distinctCounts[0].get(
      "distinctCrimeEvidence"
    );
    // code for charts ....
    const monthlyStats = await Crimes.findAll({
      attributes: [
        [literal("DATE_FORMAT(crimedate, '%b')"), "month"],
        [fn("SUM", col("id")), "totalCrime"],
        [fn("COUNT", col("crimetype")), "totalCrimeType"],
        [fn("SUM", col("id")), "totalcriminal"],
      ],
      group: literal("DATE_FORMAT(crimedate, '%b')"),
    });
    console.log(monthlyStats);
    // Send the response with all counts
    res.json({
      Status: "Success",
      monthlyStats,
      distinctCrimeType,
      distinctCrimeLocation,
      distinctCrimeEvidence,
      totalCrime,
    });
  } catch (error) {
    console.error("Error fetching crime data:", error);
    res.status(500).json({ error: "Internal server error" });
  }
};
