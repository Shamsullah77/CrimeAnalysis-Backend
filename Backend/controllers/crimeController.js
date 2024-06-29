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
