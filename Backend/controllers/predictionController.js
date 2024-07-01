const { spawn } = require('child_process');
const path = require('path');

exports.runPrediction = (req, res) => {
    const pythonProcess = spawn('python', [path.join(__dirname, '../../AiModel/predict.py')]);

    let dataString = '';

    pythonProcess.stdout.on('data', (data) => {
        dataString += data.toString();
    });

    pythonProcess.stdout.on('end', () => {
        console.log('Raw data received from Python script:', dataString.trim());
        try {
            const prediction = JSON.parse(dataString.trim());
            console.log('Parsed prediction:', prediction);
            res.json(prediction);
        } catch (err) {
            console.error('Error parsing JSON:', err);
            res.status(500).json({ error: 'Error parsing JSON' });
        }
    });

    pythonProcess.stderr.on('data', (data) => {
        console.error(`stderr: ${data}`);
        res.status(500).json({ error: data.toString() });
    });

    pythonProcess.on('close', (code) => {
        console.log(`child process exited with code ${code}`);
    });
};
