const Crime = require("../models/crimes");
const CrimeType = require("../models/crimeType");
const location = require("../models/location");
const upload = require("../middleware/upload");

exports.getcrimedata = (req, res) => {
  upload(req, res, async (err) => {
    if (err) {
      return res.status(400).json({ Status: "Error", message: err });
    }

    const {
      cases,
      crimedate,
      strategy,
      criminalid,
      crimetype,
      province,
      district,
      village,
      weather,
      temperature,
      latitude,
      longitude,
    } = req.body;

    console.log(
      cases,
      crimedate,
      strategy,
      criminalid,
      crimetype,
      province,
      district,
      village,
      weather,
      temperature,
      latitude,
      longitude
    );

    // Image data from multer
    const image = req.file ? req.file.buffer : null;

    try {
      // insert crime type.....
      const newcrimetyep = await CrimeType.create({
        Crimetype: crimetype,
      });
      const crimetypeId = newcrimetyep.id;
      console.log("CrimeType ID:", crimetypeId);
      const uid = 1;
      const newcrime = await Crime.create({
        Casees: cases,
        Crimedate: crimedate,
        Strategy: strategy,
        criminalid: criminalid,
        crimetypeid: crimetypeId,
        userid: uid,
      });
      const crimeId = newcrime.id;
      console.log("Crime ID:", crimeId);
      const newcrimelocation = await location.create({
        province: province,
        District: district,
        Village: village,
        Weather: weather,
        Temperature: temperature,
        Latitude: latitude,
        Longitude: longitude,
        Areaimage: image,
        crimeId: crimeId,
      });

      const locationid = newcrimelocation.id;
      console.log("Crimelocation id:", locationid);
      res.status(201).json({ Status: "Success" });
    } catch (error) {
      console.error("Error saving criminal data:", error);
      res.status(500).json({ Status: "Error", message: "Could not save data" });
    }
  });
};

exports.getcrimedashboard = async (req, res) => {
  try {
    const crimes = await Crime.findAll({
      attributes: ["id", "Casees", "Crimedate", "Strategy"], // Limit the number of results to 3
    });
    // Map over criminals to convert image buffer to base64
    const crimesWithBase64 = crimes.map((crime) => ({
      Id: crime.id,
      cases: crime.Casees,
      crimedate: crime.Crimedate,
      startegy: crime.Strategy,
    }));

    // console.log(usersWithBase64);
    res.json({ Status: "Success", crimes: crimesWithBase64 });
  } catch (error) {
    console.error("Error fetching crime:", error);
    res.status(500).json({ error: "Internal server error" });
  }
};
//getcrimeseemore
exports.getcrimeseemore = async (req, res) => {
  const { id } = req.query;
  console.log(id);
  try {
    const crime = await Crime.findOne({
      where: { id: id },
      attributes: ["id", "Casees", "Crimedate", "Strategy"], // Limit the number of results to 3
    });
    // Map over criminals to convert image buffer to base64
    const crimesWithBase64 = {
      id: crime.id,
      cases: crime.Casees,
      crimedate: crime.Crimedate,
      startegy: crime.Strategy,
    };

    res.json({ Status: "Success", crimes: crimesWithBase64 });
  } catch (error) {
    console.error("Error fetching crime:", error);
    res.status(500).json({ error: "Internal server error" });
  }
};
