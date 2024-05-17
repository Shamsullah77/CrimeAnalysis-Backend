const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const path = require('path');
const app = express();
const userRoutes = require('./routes/userRoutes');

const PORT = process.env.PORT || 3002;

app.use(express.static('public'));
app.use(bodyParser.json());
app.use(cors());

app.use(userRoutes);

app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});































// const express = require("express");
// const bodyParser = require("body-parser");
// const path = require("path");
// const cors = require("cors");
// const mongoose = require("mongoose");
// const app = express();
// app.set("view engine", "ejs");
// app.set("views", "views");
// app.use(bodyParser.urlencoded({ extended: false }));
// app.use(express.static(path.join(__dirname, "public")));
// app.use(express.static("public"));

// const tf = require('@tensorflow/tfjs');
// const fs = require('fs');





// const PORT = process.env.PORT || 3002;

// app.use(bodyParser.json());
// app.use(cors());

// // Connect to MongoDB
// mongoose.connect("mongodb://localhost:27017/CAPS", {
//   useNewUrlParser: true,
//   useUnifiedTopology: true,
// });
// const db = mongoose.connection;
// db.on("error", console.error.bind(console, "MongoDB connection error:"));
// db.once("open", () => {
//   console.log("Connected to MongoDB");
// });

// // Define User schema
// const userSchema = new mongoose.Schema({
//   Name: String,
//   Email: String,
//   Password: String,
//   ConfirmPassword: String,
// });

// // Add analysis schema
// const analysisSchema = new mongoose.Schema({
//     Crime_type: String,
//     Crime_date: String,
//     Crime_location: String,
//     Gender: String,
//   });

// //Crime table schema
// const crimeSchema =new mongoose.Schema({
//     crimeType:String,
//     crimeTime: String,
//     crimeLocation: String,
//     guiltyName: String,
//     guiltyGender: String,
//     guiltySSN: String,
//     guiltyProvince: String,
//     guiltyPhoneNumber: String,
//     evidence: String,
//     areaPoliceOfficer: String,
//     crimeHardness: String,
//     crimeRemark: String,
//     criminalPlacePictures: [],
//     guiltyImage: String,
// })

// //chate system schema
// const chateSchema = new mongoose.Schema({
//   Crime_type: String,
//   crimeArea:String,
//   crimeHardness:String,
//   criminals:String,
//   message:String,
// });

// const User = mongoose.model("User", userSchema);
// const Analysis = mongoose.model("Analysis", analysisSchema);
// const Crime = mongoose.model("Crime", crimeSchema);
// const chate = mongoose.model("Chate", chateSchema);



// // Routes
// app.get("/users", async (req, res) => {
//   try {
//     const users = await User.find();
//     res.json(users);
//   } catch (error) {
//     console.error(error);
//     res.status(500).json({ message: "Server error" });
//   }
// });


// app.post("/addusers", async (req, res) => {
//     try {
//       const newUser = new User(req.body);
//       await newUser.save();
//       res.json({ message: "User added successfully" });
//     } catch (error) {
//       console.error(error);
//       res.status(500).json({ message: "Server error" });
//     }
//   });

  
  
// // Route to handle analysis data
// app.post("/addanalysis", async (req, res) => {
//     try {
//       const newAnalysis = new Analysis(req.body);
//       await newAnalysis.save();
//       res.json({ message: "Analysis data added successfully" });
//     } catch (error) {
//       console.error(error);
//       res.status(500).json({ message: "Server error", error: error.message });
//     }
//   });


//   // Route to handle Crime data
// app.post("/addcrime", async (req, res) => {
//     try {
//       const newCrime = new Crime(req.body);
//       await newCrime.save();
//       res.json({ message: "Crime data added successfully" });
//     } catch (error) {
//       console.error(error);
//       res.status(500).json({ message: "Server error", error: error.message });
//     }
//   });


//   app.post('/chat', (req, res) => {
//     const { message } = req.body;
//     // Handle submission and store data in MongoDB
//     res.status(200).send('Message submitted successfully');
//   });





//   // Load JSON data
// const jsonData = JSON.parse(fs.readFileSync('./data/crime_data.json', 'utf8'));

// // Extract input features (xs) and output labels (ys) from JSON data
// const xs = [];
// const ys = [];
// const zs = [];
// jsonData.forEach(entry => {
//   const x = [
//     entry.crimetype ? 1 : 0,
//     entry.crimestrategy ? 1 : 0,
//     entry.location  ? 1 : 0,
//     entry.time_of_day ? 1 : 0,
//     entry.weather ? 1 : 0,
//     entry.socioeconomic_factors.poverty_rate,
//     entry.socioeconomic_factors.unemployment_rate,
//     entry.historical_crime_data.previous_year_crime_rate,
//     entry.historical_crime_data.previous_month_crime_rate
//   ];
//   xs.push(x);
//   // Label is the probability of a crime +ccurring
//   ys.push(entry.socioeconomic_factors.poverty_rate);
  

// });

// // Convert xs and ys to tensors
// const xsTensor = tf.tensor(xs);
// const ysTensor = tf.tensor(ys);

// console.log(ys);

// // Define the model architecture
// const model = tf.sequential();
// model.add(tf.layers.dense({ units: 64, inputShape: [xs[0].length], activation: 'relu' }));
// model.add(tf.layers.dense({ units: 32, activation: 'relu' }));
// model.add(tf.layers.dense({ units: 1, activation: 'linear' })); // Changed activation to linear

// // Compile the model
// model.compile({
//   optimizer: 'adam',
//   loss: 'meanSquaredError', // Keep mean squared error for now
// });


// // Train the model
// async function trainModel() {
//   try {
//     console.log('Training started...');
//     await model.fit(xsTensor, ysTensor, {
//       epochs: 50,
//       shuffle: true,
//       validationSplit: 0.2,
//     });
//     console.log('Training complete!');
//   } catch (error) {
//     console.error('Error during training:', error);
//   }
// }

// // Make predictions with crime details
// async function makePredictions() {
//   try {
//     console.log('Making predictions...');
//     const futurePredictions = [];
//     for (const entry of jsonData) {
//       const x = [
//         entry.crimetype ? 1 : 0,
//         entry.crimestrategy ? 1 : 0,
//         entry.location  ? 1 : 0,
//         entry.time_of_day  ? 1 : 0,
//         entry.weather  ? 1 : 0,
//         entry.socioeconomic_factors.poverty_rate,
//         entry.socioeconomic_factors.unemployment_rate,
//         entry.historical_crime_data.previous_year_crime_rate,
//         entry.historical_crime_data.previous_month_crime_rate
//       ];
//       const xTensor = tf.tensor2d([x]);
//       const prediction = model.predict(xTensor).arraySync()[0][0];
      
//       const predictedCrime = {
       
//         predicted_probability: prediction
//       };
//       futurePredictions.push(predictedCrime);
//     }
//     console.log('Predictions with crime details:');
//      console.log(futurePredictions)
   
//   } catch (error) {
//     console.error('Error during predictions:', error);
//   }
// }

// // Train the model and make predictions
// trainModel().then(() => {
//   makePredictions().then(() => {
//     console.log('Predictions complete!');
//   });
// });
  
// // Start the server
// app.listen(PORT, () => {
//   console.log(`Server is running on http://localhost:${PORT}`);
// });





