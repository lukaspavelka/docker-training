'use strict';

const express = require('express');

// Constants
const PORT = process.env.PORT || 3000; // Use environment variable for port or default to 3000
const HOST = '0.0.0.0';

// App
const app = express();
app.get('/', (req, res) => {
  res.send('Hello from a Node.js Express app in Docker!');
});

app.listen(PORT, HOST, () => {
  console.log(`Running on http://${HOST}:${PORT}`);
});
