const Criminal = require("../models/Criminal");
const upload = require("../middleware/upload");

exports.getcriminaldata = (req, res) => {
  upload(req, res, async (err) => {
    if (err) {
      return res.status(400).json({ Status: "Error", message: err });
    }

    const {
      name,
      f_name,
      dob,
      experience,
      economical_situation,
      education_level,
      phone,
      ssn,
      gender,
      province,
    } = req.body;

    // Image data from multer
    const image = req.file ? req.file.buffer : null;

    try {
      const newCriminal = await Criminal.create({
        Name: name,
        Fname: f_name,
        Province: province,
        Dob: dob,
        Experience: experience,
        Economical_situation: economical_situation,
        Education_level: education_level,
        Phone: phone,
        Ssn: ssn,
        Gender: gender,
        Image: image,
      });

      res.status(201).json({ Status: "Success" });
    } catch (error) {
      console.error("Error saving criminal data:", error);
      res.status(500).json({ Status: "Error", message: "Could not save data" });
    }
  });
};
