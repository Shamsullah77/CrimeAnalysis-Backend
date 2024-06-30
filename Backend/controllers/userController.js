const bcrypt = require("bcryptjs");
const jwt = require("jsonwebtoken");
const User = require("../models/users");
const Criminal = require("../models/Criminal");
const Userfeedback = require("../models/userfeedback");

//here is authuntication policy applied
exports.signup = async (req, res) => {
  const { Name, Email, Password, ConfirmPassword } = req.body;
  // Check if passwords match
  if (Password !== ConfirmPassword) {
    return res.json({ error: "Passwords do not match" });
  }
  try {
    // Check if the email already exists in the database
    const existingUser = await User.findOne({ where: { email: Email } });
    if (existingUser) {
      return res.json({ error: "Email address is already in use" });
    }
    // Create the new user
    const newuser = await User.create({
      Name: Name,
      Email: Email,
      Password: Password,
    });
    res.json({ Status: "Success" });
  } catch (error) {
    console.error("Error creating user:", error);
    res.status(400).json({ error: error.message });
  }
};

exports.signin = async (req, res) => {
  const { email, password } = req.body;
  try {
    const user = await User.findOne({ where: { Email: email } });

    if (!user) {
      return res.json({ error: "Invalid email or password" });
    }

    const isMatch = await bcrypt.compare(password, user.Password);
    if (!isMatch) {
      return res.json({ error: "Password Does Not Match" });
    }
    // Generate JWT token
    const uid = user.id;
    const token = jwt.sign({ uid }, "jwt-secret-key", { expiresIn: "1h" });
    res.json({ Status: "Success", token, uid });
  } catch (error) {
    console.error("Error signing in:", error);
    res.status(500).json({ error: "Server error" });
  }
};
exports.home = async (req, res) => {
  try {
    const criminals = await Criminal.findAll({
      attributes: ["Name", "Experience", "Image"], // Limit the number of results to 3
    });
    // Map over criminals to convert image buffer to base64
    const criminalsWithBase64 = criminals.map((criminal) => ({
      name: criminal.Name,
      experience: criminal.Experience,
      image: criminal.Image
        ? `data:image/jpeg;base64,${criminal.Image.toString("base64")}` // Use correct property name
        : null,
    }));

    // console.log(criminalsWithBase64);
    res.json({ Status: "Success", criminalsWithBase64 });
  } catch (error) {
    console.error("Error fetching criminals:", error);
    res.status(500).json({ error: "Internal server error" });
  }
};

exports.about = (req, res) => {
  res.json({ Status: "Success" });
};

exports.getuserdashboard = async (req, res) => {
  try {
    const users = await User.findAll({
      attributes: ["id", "Name", "Email", "Password", "role", "image"], // Limit the number of results to 3
    });
    // Map over criminals to convert image buffer to base64
    const usersWithBase64 = users.map((user) => ({
      id: user.id,
      name: user.Name,
      email: user.Email,
      password: user.Password,
      role: user.role,
      Image: user.image
        ? `data:image/jpeg;base64,${user.image.toString("base64")}` // Use correct property name
        : null,
    }));

    // console.log(criminalsWithBase64);
    res.json({ Status: "Success", users: usersWithBase64 });
  } catch (error) {
    console.error("Error fetching criminals:", error);
    res.status(500).json({ error: "Internal server error" });
  }
};

exports.deleteuserdashboard = async (req, res) => {
  const { userId } = req.body;

  console.log(userId);
  try {
    // Find the user by userId
    const existingUser = await User.findOne({ where: { id: userId } });
    console.log(existingUser);
    // If the user doesn't exist, send a 404 response
    if (!existingUser) {
      return res.status(404).send({ message: "User not found" });
    }

    // Delete the user
    await existingUser.destroy();

    res.json({ Status: "Success" });
  } catch (error) {
    console.error("Error creating user:", error);
    res.status(400).json({ error: error.message });
  }
};
exports.userfeedback = async (req, res) => {
  const { feedback, id } = req.body;
  console.log(feedback, id);
  const newfeedback = await Userfeedback.create({
    userId: id,
    feedback: feedback,
  });
  res.json({ Status: "Success" });
};
