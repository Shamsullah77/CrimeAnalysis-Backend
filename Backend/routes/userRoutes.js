const express = require("express");
const router = express.Router();
const authcontroller = require("../controllers/userController");
const is_auth = require("../middleware/is-auth");
const contactcontroller = require("../controllers/contactcontroller");
const analysiscontroller = require("../controllers/analysiscontroller");
const dashcontroller = require("../controllers/dashboardcontroller");
const criminalcontroller = require("../controllers/criminalController");
const crimecontroller = require("../controllers/crimeController");
const victimcontroller = require("../controllers/victimcontroller");
router.post("/signup", authcontroller.signup);
router.post("/signin", authcontroller.signin);
router.get("/", authcontroller.home);
router.get("/About", authcontroller.about);
router.get("/crimeanalysis", analysiscontroller.analysiseddata);
router.get("/contactus", contactcontroller.getcontact);
router.post("/formdata", analysiscontroller.analysisformdata);
// criminals routes
router.post("/criminaldata", criminalcontroller.getcriminaldata);
router.get("/getcriminalinfo", criminalcontroller.getcriminalinfo);
// crime routes
router.post("/crimedata", crimecontroller.getcrimedata);
// victim routes
router.get("/getvictim", victimcontroller.getvictim);
router.post("/victimdata", victimcontroller.getvictimdata);
// dashboard routes .................

router.get("/maindashboard", dashcontroller.dashboard);
module.exports = router;
