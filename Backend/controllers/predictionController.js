const { spawn } = require('child_process');
const path = require('path');

function runScript(scriptPath, res) {
  console.log(`Running script: ${scriptPath}`);
  
  // Set the working directory to the directory of the script
  const scriptDir = path.dirname(scriptPath);
  
  // Spawn the Python process
  const process = spawn('python', [scriptPath], { cwd: scriptDir });

  let scriptOutput = '';

  process.stdout.on('data', (data) => {
    console.log(`stdout: ${data}`);
    scriptOutput += data.toString();
  });

  process.stderr.on('data', (data) => {
    console.error(`stderr: ${data}`);
    res.status(500).send(`Error: ${data.toString()}`);
  });

  process.on('close', (code) => {
    if (code === 0) {
      res.status(200).send(scriptOutput);
    } else {
      res.status(500).send(`Script exited with code ${code}`);
    }
  });
}

exports.runPreprocess = (req, res) => {
  const scriptPath = path.join(__dirname, '../../AiModel/preprocess.py');
  runScript(scriptPath, res);
};

exports.runModelTraining = (req, res) => {
  const scriptPath = path.join(__dirname, '../../AiModel/AiPreprocessingModelTraining.py');
  runScript(scriptPath, res);
};

exports.runPrediction = (req, res) => {
  const scriptPath = path.join(__dirname, '../../AiModel/predict.py');
  runScript(scriptPath, res);
};
