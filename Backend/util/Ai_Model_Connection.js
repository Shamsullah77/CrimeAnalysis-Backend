const express = require('express');
const bodyParser = require('body-parser');
const { PythonShell } = require('python-shell');

const app = express();
const port = 3002;

app.use(bodyParser.json());

app.post('/predict', (req, res) => {
  let data = req.body;

  console.log("Received data for prediction:", data); // Log received data

  PythonShell.run('../../AiModel/AiModel/Connection.py', { args: [JSON.stringify(data)] }, (err, result) => {
    if (err) {
      console.error("Error occurred during Python script execution:", err);
      res.status(500).send('Error occurred during prediction.');
    } else {
      console.log("Python script output:", result); // Log Python script output
      let predictions;
      try {
        predictions = JSON.parse(result[0]);
        res.send(predictions);
      } catch (parseError) {
        console.error("Error parsing Python script output:", parseError);
        res.status(500).send('Error parsing prediction results.');
      }
    }
  });
});

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});
