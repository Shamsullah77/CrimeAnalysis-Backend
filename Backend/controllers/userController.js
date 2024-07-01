const bcrypt = require("bcryptjs");
const jwt = require("jsonwebtoken");
const User = require("../models/users");
const Criminal = require("../models/Criminal");
const Userfeedback = require("../models/userfeedback");
const Feedback = require("../models/userfeedback");

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
    const urole = user.role;

    const token = jwt.sign({ uid }, "jwt-secret-key", { expiresIn: "1h" });
    res.json({ Status: "Success", token, uid, urole });
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
    // criminals over home page
    const criminalsWithBase64 = criminals.map((criminal) => ({
      name: criminal.Name,
      experience: criminal.Experience,
      image: criminal.Image
        ? `data:image/jpeg;base64,${criminal.Image.toString("base64")}` // Use correct property name
        : null,
    }));
    // users feedback over home page
    const feedback = await Feedback.findAll({
      attributes: ["feedbackId", "userId", "feedback"],
      include: [
        {
          model: User,
          attributes: ["Name", "image"],
          required: true, // Ensures that only feedback with associated user is returned
        },
      ],
    });
    // Map over criminals to convert image buffer to base64
    const feedbackWithUserDetails = feedback.map((item) => ({
      feedback: item.feedback,
      username: item.User.Name,
      userimage: item.User.image
        ? `data:image/jpeg;base64,${item.User.image.toString("base64")}` // Use correct property name
        : null,
    }));

    res.json({
      Status: "Success",
      criminalsWithBase64,
      userfeedbacks: feedbackWithUserDetails,
    });
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
exports.getuserfeedback = async (req, res) => {
  try {
    const feedback = await Feedback.findAll({
      attributes: ["feedbackId", "userId", "feedback"],
      include: [
        {
          model: User,
          attributes: ["Name", "image"],
          required: true, // Ensures that only feedback with associated user is returned
        },
      ],
    });
    // Map over criminals to convert image buffer to base64
    const feedbackWithUserDetails = feedback.map((item) => ({
      feedbackId: item.feedbackId,
      feedback: item.feedback,
      username: item.User.Name,
      userimage: item.User.image
        ? `data:image/jpeg;base64,${item.User.image.toString("base64")}` // Use correct property name
        : null,
    }));

    // console.log(criminalsWithBase64);
    res.json({ Status: "Success", feedback: feedbackWithUserDetails });
  } catch (error) {
    console.error("Error fetching criminals:", error);
    res.status(500).json({ error: "Internal server error" });
  }
};

exports.deleteuserfeedback = async (req, res) => {
  const { feedbackId } = req.body;

  console.log(feedbackId);
  try {
    // Find the user by userId
    const existingfeedback = await Feedback.findOne({
      where: { feedbackId: feedbackId },
    });
    // Delete the user
    await existingfeedback.destroy();
    const feedback = await Feedback.findAll({
      attributes: ["feedbackId", "userId", "feedback"],
      include: [
        {
          model: User,
          attributes: ["Name", "image"],
          required: true, // Ensures that only feedback with associated user is returned
        },
      ],
    });
    // Map over criminals to convert image buffer to base64
    const feedbackWithUserDetails = feedback.map((item) => ({
      feedbackId: item.feedbackId,
      feedback: item.feedback,
      username: item.User.Name,
      userimage: item.User.image
        ? `data:image/jpeg;base64,${item.User.image.toString("base64")}` // Use correct property name
        : null,
    }));

    // console.log(criminalsWithBase64);
    res.json({ Status: "Success", feedback: feedbackWithUserDetails });
  } catch (error) {
    console.error("Error creating user:", error);
    res.status(400).json({ error: error.message });
  }
};
//getuserseemore
exports.getuserseemore = async (req, res) => {
  const { id } = req.query;
  console.log(id);
  try {
    const user = await User.findOne({
      where: { id: id },
      attributes: ["id", "Name", "Email", "Password", "role", "image"],
    });
    console.log(user);
    if (!user) {
      return res.status(404).json({ error: "User not found" });
    }

    // Convert image buffer to base64 if it exists
    const userWithBase64 = {
      id: user.id,
      name: user.Name,
      email: user.Email,
      password: user.Password,
      role: user.role,
      image: user.image
        ? `data:image/jpeg;base64,${user.image.toString("base64")}`
        : null,
    };

    res.json({ status: "Success", user: userWithBase64 });
  } catch (error) {
    console.error("Error fetching victim:", error);
    res.status(500).json({ error: "Internal server error" });
  }
};

//getvictimupdates
exports.getuserupdate = async (req, res) => {
  const { Id } = req.query;
  console.log("user id is " + Id);
  try {
    const user = await User.findOne({
      where: { id: Id },
      attributes: ["Name", "Email", "role", "image"],
    });

    if (!user) {
      return res.status(404).json({ error: "user not found" });
    }

    // Convert image buffer to base64 if it exists
    const userWithBase64 = {
      id: user.id,
      name: user.Name,
      image: user.image
        ? `data:image/jpeg;base64,${user.image.toString("base64")}`
        : null,
      email: user.Email,
      role: user.role,
    };
    // console.log(userWithBase64);
    res.json({ Status: "Success", user: userWithBase64 });
  } catch (error) {
    console.error("Error fetching victim:", error);
    res.status(500).json({ error: "Internal server error" });
  }
};

//getvictimupdatesubmit
exports.getuserupdatesubmit = async (req, res) => {
  console.log("i am here");
  const { Name, Image, Email, Role } = req.body;
  console.log(Name, Email, Role);
  try {
    const user = await User.findOne({ where: { Email: Email } });

    if (!user) {
      return res.status(404).json({ error: "user not found" });
    }

    await User.update(
      { Name, Image, Role, Email },
      { where: { Email: Email } }
    );

    res.json({ status: "Success" });
  } catch (error) {
    console.error("Error updating user:", error);
    res.status(500).json({ error: "Internal server error" });
  }
};
