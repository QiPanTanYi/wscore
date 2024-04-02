const { app, BrowserWindow, ipcMain } = require('electron');
const path = require('path'); // 引入 path 模块
const fs = require('fs'); // 引入 fs 模块

function createWindow() {
  // 创建浏览器窗口
  let mainWindow = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      preload: path.join(__dirname, 'preload.js') // 指定 preload 脚本的路径
    }
  });

  // 加载 index.html 文件
  mainWindow.loadFile('index.html');

  // 监听 did-finish-load 事件，在每个页面加载完成后执行注入脚本的操作
  mainWindow.webContents.on('did-finish-load', () => {
    // 读取 wr.js 文件的内容
    const scriptPath = path.join(__dirname, 'wr.js');
    
    fs.readFile(scriptPath, 'utf8', (err, data) => {
      if (err) {
        console.error(err);
        return;
      }
      
      // 在每个页面中执行注入脚本的操作
      mainWindow.webContents.executeJavaScript(data);
    });
  });

  // 当窗口关闭时，触发 'closed' 事件
  mainWindow.on('closed', () => {
    // 取消对窗口对象的引用，如果你的应用支持多窗口，通常会将窗口存储在数组中，这里应删除相应的元素
    mainWindow = null;
  });
}

app.on('ready', createWindow);
app.on('window-all-closed', () => {
  console.log('All windows are closed');
  app.quit();
});
app.on('activate', () => {
  if (BrowserWindow.getAllWindows().length === 0) {
    createWindow();
  }
});
