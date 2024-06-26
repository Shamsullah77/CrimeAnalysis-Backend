const express = require("express");
const router = express.Router();
const authcontroller = require("../controllers/userController");
const is_auth = require("../middleware/is-auth");
const contactcontroller = require("../controllers/contactcontroller");
const analysiscontroller = require("../controllers/analysiscontroller");
const dashcontroller = require("../controllers/dashboardcontroller");

router.post("/signup", authcontroller.signup);
router.post("/signin", authcontroller.signin);
router.get("/", authcontroller.home);
router.get("/About", authcontroller.about);
router.get("/crimeanalysis", analysiscontroller.analysiseddata);
router.get("/contactus", contactcontroller.getcontact);
router.post("/formdata", analysiscontroller.analysisformdata);
// dashboard routes .................

router.get("/maindashboard", dashcontroller.dashboard);
module.exports = router;
