const { app, BrowserWindow, ipcMain } = require('electron');
const path = require('path');
const { spawn } = require('child_process');
const axios = require('axios');

let mainWindow;
let pythonProcess;

function createWindow() {
    mainWindow = new BrowserWindow({
        width: 1200,
        height: 800,
        webPreferences: {
            nodeIntegration: true,
            contextIsolation: false
        }
    });

    mainWindow.loadFile('index.html');
}

app.whenReady().then(() => {
    createWindow();

    // Python API'sini başlat
    pythonProcess = spawn('python', ['api.py']);
    
    pythonProcess.stdout.on('data', (data) => {
        console.log(`Python API: ${data}`);
    });

    pythonProcess.stderr.on('data', (data) => {
        console.error(`Python API Error: ${data}`);
    });
});

app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') {
        app.quit();
    }
});

app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) {
        createWindow();
    }
});

// Uygulama kapatılırken Python API'sini de kapat
app.on('before-quit', () => {
    if (pythonProcess) {
        pythonProcess.kill();
    }
}); 