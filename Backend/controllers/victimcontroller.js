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
