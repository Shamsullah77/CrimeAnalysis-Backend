// Middleware to check if user is authenticated
const jwt = require("jsonwebtoken");
const User = require("../models/users");
exports.AuthUser = async (req, res, next) => {
  const token = req.headers["access-token"];
  if (!token) {
    return res.json("need token");
  } else {
    jwt.verify(token, "jwt-secret-key", async (err, decoded) => {
      if (err) {
        console.log("err");
        return res.json("not auth");
      } else {
        const user = await User.findByPk(decoded.uid);
        req.user = user;

        next();
      }
    });
  }
};
// Middleware to check if user is has the permission to the route
exports.AuthRole = (role) => {
  return (req, res, next) => {
    if (role.includes(req.user.role)) {
      next();
    } else {
      res.json({ Status: "Fail" });
    }
  };
};
