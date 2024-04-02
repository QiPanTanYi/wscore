const { contextBridge, ipcRenderer } = require('electron');
const fs = require('fs');
const path = require('path');

// 在 contextBridge 中将 fs、path 模块暴露给渲染进程
contextBridge.exposeInMainWorld('electron', {
  fs: fs,
  path: path
});
