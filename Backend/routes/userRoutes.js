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
const dataController = require("../controllers/dataController");
const crimefromothersource = require("../controllers/crimefromothersourcecontroller");
const crime = require("../models/crimes");
//user routes
router.post("/signup", authcontroller.signup);
router.post("/signin", authcontroller.signin);
router.get("/getuserdashboard", authcontroller.getuserdashboard);
router.post("/deleteuser", authcontroller.deleteuserdashboard);
router.post("/userfeedback", authcontroller.userfeedback);
router.get("/getfeedbackdashboard", authcontroller.getuserfeedback);
router.post("/deleteuserfeedback", authcontroller.deleteuserfeedback);
router.get("/getuserseemore", authcontroller.getuserseemore);
router.get("/getuserupdate", authcontroller.getuserupdate);
router.post("/getuserupdatesubmit", authcontroller.getuserupdatesubmit);
router.get("/", authcontroller.home);
router.get("/About", authcontroller.about);
//crime analysis routes
router.get(
  "/crimeanalysis",
  is_auth.AuthUser,
  is_auth.AuthRole("admin"),
  analysiscontroller.analysiseddata
);
router.get("/contactus", contactcontroller.getcontact);
router.post("/formdata", analysiscontroller.analysisformdata);
// criminals routes
router.post("/criminaldata", criminalcontroller.getcriminaldata);
router.get("/getcriminals",criminalcontroller.getCriminals);
router.get("/getcriminalinfo", criminalcontroller.getcriminalinfo);
router.get("/getcriminaldashboard", criminalcontroller.getcriminaldashboard);
router.post("/deletecriminal", criminalcontroller.deletecriminal);
router.get("/getcriminalseemore", criminalcontroller.getcriminalseemore);
router.get("/getcriminalupdate", criminalcontroller.getcriminalupdate);
router.post(
  "/getcriminalupdatesubmit",
  criminalcontroller.getcriminalupdatesubmit
);
// crime from other source route
router.post(
  "/crimefromothersourcedata",
  crimefromothersource.getcrimefromothesource
);
router.get(
  "/getcrimefromothersourcedata",
  crimefromothersource.getCrimeFromOtherSourcedata
);
router.delete("/deletecrime/:id", crimefromothersource.deleteCrimeById);
router.get("/savedatatojson", crimefromothersource.saveDataToJson);

// crime routes
router.post("/crimedata", crimecontroller.getcrimedata);
router.get("/getcrimedashboard", crimecontroller.getcrimedashboard);
router.get("/getcrimeseemore", crimecontroller.getcrimeseemore);
router.get("/getcrimeupdate", crimecontroller.getcrimeupdate);
router.post("/getcrimeupdatesubmit", crimecontroller.getcrimeupdatesubmit);
// victim routes
router.get("/getvictim", victimcontroller.getvictim);
router.post("/victimdata", victimcontroller.getvictimdata);
router.get("/getvictimdashboard", victimcontroller.getvictimdashboard);
router.post("/deletevictim", victimcontroller.deletevictim);
router.get("/getvictimupdate", victimcontroller.getvictimupdate);
router.get("/getvictimseemore", victimcontroller.getvictimseemore);
router.post("/getvictimupdatesubmit", victimcontroller.getvictimupdatesubmit);
router.post("/load-data", dataController.loadData);
// dashboard routes .................
router.get(
  "/maindashboard",
  is_auth.AuthUser,
  is_auth.AuthRole("admin"),
  dashcontroller.dashboard
);
router.get("/getreportdata", dashcontroller.reportresult);
// maps routes
router.get("/api/location/crimes", crimecontroller.getLocationCrimes);
module.exports = router;

// Backend/routes/dataRoutes.js
