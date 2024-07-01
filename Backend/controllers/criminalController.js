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

// Controller to handle getting criminal info
exports.getcriminalinfo = async (req, res) => {
  const { name } = req.query; // Get the name from the query parameters
  console.log(name);

  try {
    const criminal = await Criminal.findOne({
      where: { Name: name },
      attributes: [
        "Name",
        "Experience",
        "Image",
        "Province",
        "Dob",
        "Economical_situation",
        "Education_level",
        "Phone",
        "Ssn",
        "Gender",
        "Image",
      ],
    });

    if (!criminal) {
      return res.status(404).json({ error: "Criminal not found" });
    }

    // Convert image buffer to base64 if it exists
    const criminalWithBase64 = {
      name: criminal.Name,
      experience: criminal.Experience,
      dob: criminal.Dob,
      economical_situation: criminal.Economical_situation,
      education_level: criminal.Education_level,
      phone: criminal.Phone,
      ssn: criminal.Ssn,
      gender: criminal.Gender,
      image: criminal.Image
        ? `data:image/jpeg;base64,${criminal.Image.toString("base64")}`
        : null,
    };

    res.json({ Status: "Success", criminal: criminalWithBase64 });
  } catch (error) {
    console.error("Error fetching criminal:", error);
    res.status(500).json({ error: "Internal server error" });
  }
};

exports.getcriminaldashboard = async (req, res) => {
  try {
    const criminal = await Criminal.findAll({
      attributes: ["id", "Name", "Fname", "Province", "Phone", "Image"], // Limit the number of results to 3
    });
    // Map over criminals to convert image buffer to base64
    const criminalWithBase64 = criminal.map((criminal) => ({
      id: criminal.id,
      name: criminal.Name,
      fname: criminal.Fname,
      province: criminal.Province,
      phone: criminal.Phone,
      image: criminal.Image
        ? `data:image/jpeg;base64,${criminal.Image.toString("base64")}` // Use correct property name
        : null,
    }));

    // console.log(criminalsWithBase64);
    res.json({ Status: "Success", criminals: criminalWithBase64 });
  } catch (error) {
    console.error("Error fetching criminals:", error);
    res.status(500).json({ error: "Internal server error" });
  }
};

exports.deletecriminal = async (req, res) => {
  const { criminalid } = req.body;
  console.log(criminalid);
  try {
    const existingcriminal = await Criminal.findOne({
      where: { id: criminalid },
    });
    // Delete the user
    await existingcriminal.destroy();

    const criminal = await Criminal.findAll({
      attributes: ["id", "Name", "Fname", "Province", "Phone", "Image"], // Limit the number of results to 3
    });
    // Map over criminals to convert image buffer to base64
    const criminalWithBase64 = criminal.map((criminal) => ({
      id: criminal.id,
      name: criminal.Name,
      fname: criminal.Fname,
      province: criminal.Province,
      phone: criminal.Phone,
      image: criminal.Image
        ? `data:image/jpeg;base64,${criminal.Image.toString("base64")}` // Use correct property name
        : null,
    }));

    // console.log(criminalsWithBase64);
    res.json({ Status: "Success", criminals: criminalWithBase64 });
    // console.log(criminalsWithBase64);
    res.json({ Status: "Success", criminals: criminalWithBase64 });
  } catch (error) {
    console.error("Error fetching criminals:", error);
    res.status(500).json({ error: "Internal server error" });
  }
};
//getcriminalseemore
exports.getcriminalseemore = async (req, res) => {
  const { id } = req.query;
  console.log(id);
  try {
    const criminal = await Criminal.findOne({
      where: { id: id },
      attributes: [
        "Name",
        "Fname",
        "Experience",
        "Image",
        "Province",
        "Dob",
        "Economical_situation",
        "Education_level",
        "Phone",
        "Ssn",
        "Gender",
        "Image",
      ],
    });

    if (!criminal) {
      return res.status(404).json({ error: "Criminal not found" });
    }

    // Convert image buffer to base64 if it exists
    const criminalWithBase64 = {
      name: criminal.Name,
      fname: criminal.Fname,
      experience: criminal.Experience,
      province: criminal.Province,
      dob: criminal.Dob,
      economical_situation: criminal.Economical_situation,
      education_level: criminal.Education_level,
      phone: criminal.Phone,
      ssn: criminal.Ssn,
      gender: criminal.Gender,
      image: criminal.Image
        ? `data:image/jpeg;base64,${criminal.Image.toString("base64")}`
        : null,
    };

    console.log(criminalWithBase64);

    res.json({ status: "Success", criminal: criminalWithBase64 });
  } catch (error) {
    console.error("Error fetching criminal:", error);
    res.status(500).json({ error: "Internal server error" });
  }
};
//getcriminalseemore
exports.getcriminalupdate = async (req, res) => {
  const { id } = req.query;
  console.log(id);
  try {
    const criminal = await Criminal.findOne({
      where: { id: id },
      attributes: [
        "id",
        "Name",
        "Fname",
        "Experience",
        "Image",
        "Province",
        "Dob",
        "Economical_situation",
        "Education_level",
        "Phone",
        "Ssn",
        "Gender",
        "Image",
      ],
    });

    if (!criminal) {
      return res.status(404).json({ error: "Criminal not found" });
    }

    // Convert image buffer to base64 if it exists
    const criminalWithBase64 = {
      id: criminal.id,
      name: criminal.Name,
      fname: criminal.Fname,
      experience: criminal.Experience,
      province: criminal.Province,
      dob: criminal.Dob,
      economical_situation: criminal.Economical_situation,
      education_level: criminal.Education_level,
      phone: criminal.Phone,
      ssn: criminal.Ssn,
      gender: criminal.Gender,
      image: criminal.Image
        ? `data:image/jpeg;base64,${criminal.Image.toString("base64")}`
        : null,
    };

    res.json({ status: "Success", criminal: criminalWithBase64 });
  } catch (error) {
    console.error("Error fetching criminal:", error);
    res.status(500).json({ error: "Internal server error" });
  }
};
//getcriminalupdatesubmit
exports.getcriminalupdatesubmit = async (req, res) => {
  const {
    id,
    name,
    fname,
    experience,
    province,
    dob,
    economical_situation,
    education_level,
    phone,
    ssn,
    gender,
    image,
  } = req.body;
  console.log(
    id,
    name,
    fname,
    experience,
    province,
    dob,
    economical_situation,
    education_level,
    phone,
    ssn,
    gender,
    image
  );

  try {
    const criminal = await Criminal.findOne({ where: { id } });

    if (!criminal) {
      return res.status(404).json({ error: "criminal not found" });
    }

    await Victim.update(
      {
        name,
        fname,
        experience,
        province,
        dob,
        economical_situation,
        education_level,
        phone,
        ssn,
        gender,
        image,
      },
      { where: { id } }
    );

    res.json({ status: "Success" });
  } catch (error) {
    console.error("Error updating victim:", error);
    res.status(500).json({ error: "Internal server error" });
  }
};
