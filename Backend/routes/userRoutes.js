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
//user routes
router.post("/signup", authcontroller.signup);
router.post("/signin", authcontroller.signin);
router.get("/getuserdashboard", authcontroller.getuserdashboard);
router.post("/deleteuser", authcontroller.deleteuserdashboard);
router.post("/userfeedback", authcontroller.userfeedback);
router.get("/getfeedbackdashboard", authcontroller.getuserfeedback);
router.post("/deleteuserfeedback", authcontroller.deleteuserfeedback);
router.get("/", authcontroller.home);
router.get("/About", authcontroller.about);
router.get("/crimeanalysis", analysiscontroller.analysiseddata);
router.get("/contactus", contactcontroller.getcontact);
router.post("/formdata", analysiscontroller.analysisformdata);
// criminals routes
router.post("/criminaldata", criminalcontroller.getcriminaldata);
router.get("/getcriminalinfo", criminalcontroller.getcriminalinfo);
router.get("/getcriminaldashboard", criminalcontroller.getcriminaldashboard);
router.post("/deletecriminal", criminalcontroller.deletecriminal);
// crime routes
router.post("/crimedata", crimecontroller.getcrimedata);
router.get("/getcrimedashboard", crimecontroller.getcrimedashboard);
// victim routes
router.get("/getvictim", victimcontroller.getvictim);
router.post("/victimdata", victimcontroller.getvictimdata);
router.get("/getvictimdashboard", victimcontroller.getvictimdashboard);
// dashboard routes .................
router.get("/maindashboard", dashcontroller.dashboard);
module.exports = router;
