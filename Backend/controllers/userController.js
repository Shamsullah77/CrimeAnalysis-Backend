const bcrypt = require("bcryptjs");
const jwt = require("jsonwebtoken");
const User = require("../models/users");

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
exports.home = (req, res) => {
  res.json({ Status: "Success" });
};
exports.about = (req, res) => {
  res.json({ Status: "Success" });
};
