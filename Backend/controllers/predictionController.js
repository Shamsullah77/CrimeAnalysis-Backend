const { spawn } = require('child_process');
const path = require('path');

exports.runPrediction = (req, res) => {
    const pythonProcess = spawn('python', [path.join(__dirname, '../AiModel/predict.py')]);
    
    pythonProcess.stdout.on('data', (data) => {
        const prediction = JSON.parse(data.toString());
        console.log(prediction);
        res.json(prediction);
    });


    pythonProcess.stderr.on('data', (data) => {
        console.error(`stderr: ${data}`);
    });

    pythonProcess.on('close', (code) => {
        console.log(`child process exited with code ${code}`);
    });
};
