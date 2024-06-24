const express = require("express");
const router = express.Router();
const authcontroller = require("../controllers/userController");
const is_auth = require("../middleware/is-auth");
const contactcontroller = require("../controllers/contactcontroller");
const analysiscontroller = require("../controllers/analysiscontroller");
const dashcontroller = require("../controllers/dashboardcontroller");

router.post("/signup", authcontroller.signup);
router.post("/signin", authcontroller.signin);
router.get("/", is_auth.AuthUser, authcontroller.home);
router.get("/About", is_auth.AuthUser, authcontroller.about);
router.get(
  "/crimeanalysis",
  is_auth.AuthUser,
  analysiscontroller.analysiseddata
);
router.get("/contactus", is_auth.AuthUser, contactcontroller.getcontact);
router.post("/formdata", is_auth.AuthUser, analysiscontroller.analysisformdata);
// dashboard routes .................

router.get("/maindashboard", dashcontroller.dashboard);
module.exports = router;
