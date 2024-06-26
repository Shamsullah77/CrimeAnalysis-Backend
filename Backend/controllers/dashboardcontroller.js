const Crimes = require("../models/crimes");
const { literal, fn, col } = require("sequelize");
const CrimeType = require("../models/crimeType");
const Location = require("../models/location");
const Criminals = require("../models/Criminal");
Crimes.belongsTo(CrimeType, { foreignKey: "crimetypeid", as: "crimetypes" });
exports.dashboard = async (req, res) => {
  try {
    //Count totals for each card
    const totallocations = await Location.findAll({
      attributes: [
        [fn("COUNT", fn("DISTINCT", col("Village"))), "totallocations"],
      ],
    });
    const totalcrimetypes = await CrimeType.findAll({
      attributes: [
        [fn("COUNT", fn("DISTINCT", col("crimetype"))), "totalcrimetypes"],
      ],
    });
    const totalcriminals = await Criminals.findAll({
      attributes: [
        [fn("COUNT", fn("DISTINCT", col("name"))), "totalcriminals"],
      ],
    });
    // Fetch total count of all crimes
    const totalCrime = await Crimes.count();

    // code for charts ....
    const monthlyStats = await Crimes.findAll({
      attributes: [
        [literal("DATE_FORMAT(crimedate, '%b')"), "month"],
        [fn("COUNT", col("userid")), "totalCrime"],
        [
          fn("COUNT", fn("DISTINCT", col("crimetypes.crimetype"))),
          "totalCrimeType",
        ],
        [fn("COUNT", col("Strategy")), "totalCrimestrategies"],
      ],
      include: [
        {
          model: CrimeType,
          as: "crimetypes",
          attributes: [],
        },
      ],
      group: [literal("DATE_FORMAT(crimedate, '%b')")],
    });

    const tlocation = totallocations[0].get("totallocations");
    const tcriminals = totalcriminals[0].get("totalcriminals");
    const tcrimetypes = totalcrimetypes[0].get("totalcrimetypes");
    console.log(tlocation, tcrimetypes, tcriminals);
    // Send the response with all counts
    res.json({
      Status: "Success",
      monthlyStats,
      totalCrime,
      tlocation,
      tcriminals,
      tcrimetypes,
    });
  } catch (error) {
    console.error("Error fetching crime data:", error);
    res.status(500).json({ error: "Internal server error" });
  }
};
