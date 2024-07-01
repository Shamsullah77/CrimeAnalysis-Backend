const victimcontroller = require("../models/victim");
const Criminal = require("../models/Criminal");
const Victim = require("../models/victim");
exports.getvictim = async (req, res) => {
  try {
    // Fetch criminals' ids and names
    const criminals = await Criminal.findAll({
      attributes: ["id", "Name"],
    });

    // Map over criminals to format the response
    const criminalData = criminals.map((criminal) => ({
      id: criminal.getDataValue("id"),
      name: criminal.getDataValue("Name"),
    }));

    res.status(201).json({ Status: "Success", criminals: criminalData });
  } catch (error) {
    console.error("Error fetching criminals:", error);
    res.status(500).json({ error: "Internal server error" });
  }
};
exports.getvictimdata = async (req, res) => {
  const { name, last_name, province, age, gender, cremenal } = req.body;

  try {
    const newVictim = await Victim.create({
      Name: name,
      Lname: last_name,
      Province: province,
      Age: age,
      Gender: gender,
      criminal: cremenal,
    });

    res.status(201).json({ Status: "Success" });
  } catch (error) {
    console.error("Error saving criminal data:", error);
    res.status(500).json({ Status: "Error", message: "Could not save data" });
  }
};

exports.getvictimdashboard = async (req, res) => {
  try {
    const victims = await Victim.findAll({
      attributes: [
        "id",
        "Name",
        "Lname",
        "Province",
        "Age",
        "Gender",
        "criminal",
      ], // Limit the number of results to 3
    });
    // Map over criminals to convert image buffer to base64
    const usersWithBase64 = victims.map((victim) => ({
      id: victim.id,
      name: victim.Name,
      lname: victim.Lname,
      province: victim.Province,
      age: victim.Age,
      gender: victim.Gender,
      Criminal: victim.criminal,
    }));

    // console.log(usersWithBase64);
    res.json({ Status: "Success", victim: usersWithBase64 });
  } catch (error) {
    console.error("Error fetching criminals:", error);
    res.status(500).json({ error: "Internal server error" });
  }
};
//deletevictim
exports.deletevictim = async (req, res) => {
  const { victimid } = req.body;
  console.log(victimid);
  try {
    // Find the user by userId
    const existingvictim = await Victim.findOne({
      where: { id: victimid },
    });
    await existingvictim.destroy();

    const victims = await Victim.findAll({
      attributes: [
        "id",
        "Name",
        "Lname",
        "Province",
        "Age",
        "Gender",
        "criminal",
      ], // Limit the number of results to 3
    });
    // Map over criminals to convert image buffer to base64
    const usersWithBase64 = victims.map((victim) => ({
      id: victim.id,
      name: victim.Name,
      lname: victim.Lname,
      province: victim.Province,
      age: victim.Age,
      gender: victim.Gender,
      Criminal: victim.criminal,
    }));

    // console.log(usersWithBase64);
    res.json({ Status: "Success", victim: usersWithBase64 });
  } catch (error) {
    console.error("Error fetching criminals:", error);
    res.status(500).json({ error: "Internal server error" });
  }
};
//getvictimseemore
exports.getvictimseemore = async (req, res) => {
  const { id } = req.query;

  try {
    const victim = await Victim.findOne({
      where: { id: id },
      attributes: ["id", "Name", "Lname", "Province", "Age", "Gender"],
      include: [
        {
          model: Criminal,
          attributes: ["id", "Name"],
          required: true, // Ensures that only feedback with associated user is returned
        },
      ], // Limit the number of results to 3
    });

    if (!victim) {
      return res.status(404).json({ error: "victim not found" });
    }

    // Convert image buffer to base64 if it exists
    const victimWithBase64 = {
      id: victim.id,
      name: victim.Name,
      lname: victim.Lname,
      province: victim.Province,
      age: victim.Age,
      gender: victim.Gender,
      criminal: victim.Criminal.Name,
      criminalid: victim.Criminal.id,
    };
    console.log(victimWithBase64);
    res.json({ Status: "Success", victim: victimWithBase64 });
  } catch (error) {
    console.error("Error fetching victim:", error);
    res.status(500).json({ error: "Internal server error" });
  }
};
//getvictimupdates
exports.getvictimupdate = async (req, res) => {
  const { id } = req.query;
  try {
    const victim = await Victim.findOne({
      where: { id: id },
      attributes: ["id", "Name", "Lname", "Province", "Age", "Gender"],
      include: [
        {
          model: Criminal,
          attributes: ["id", "Name"],
          required: true, // Ensures that only feedback with associated user is returned
        },
      ], // Limit the number of results to 3
    });

    if (!victim) {
      return res.status(404).json({ error: "victim not found" });
    }

    // Convert image buffer to base64 if it exists
    const victimWithBase64 = {
      id: victim.id,
      name: victim.Name,
      lname: victim.Lname,
      province: victim.Province,
      age: victim.Age,
      gender: victim.Gender,
      criminal: victim.Criminal.Name,
      criminalid: victim.Criminal.id,
    };
    console.log(victimWithBase64);
    res.json({ Status: "Success", victim: victimWithBase64 });
  } catch (error) {
    console.error("Error fetching victim:", error);
    res.status(500).json({ error: "Internal server error" });
  }
};

//getvictimupdatesubmit
exports.getvictimupdatesubmit = async (req, res) => {
  const { ID, Name, L_Name, Province, Age, Gender } = req.body;

  try {
    const victim = await Victim.findOne({ where: { ID } });

    if (!victim) {
      return res.status(404).json({ error: "Victim not found" });
    }

    await Victim.update(
      { Name, L_Name, Province, Age, Gender },
      { where: { ID } }
    );

    res.json({ status: "Success" });
  } catch (error) {
    console.error("Error updating victim:", error);
    res.status(500).json({ error: "Internal server error" });
  }
};
