// Simple Node.js proxy for Overpass API
const express = require('express');
const fetch = require('node-fetch');
const bodyParser = require('body-parser');
const app = express();
const PORT = process.env.PORT || 3000;

app.use(bodyParser.text({ type: '*/*', limit: '1mb' }));

// Proxy endpoint for Overpass API
app.post('/api/overpass', async (req, res) => {
  try {
    const overpassUrl = 'https://overpass-api.de/api/interpreter';
    const response = await fetch(overpassUrl, {
      method: 'POST',
      headers: { 'Content-Type': 'text/plain' },
      body: req.body
    });
    const data = await response.text();
    res.set('Content-Type', 'application/json');
    res.send(data);
  } catch (err) {
    res.status(500).json({ error: 'Proxy error', details: err.message });
  }
});

// Serve static files (index.html, etc.)
app.use(express.static(__dirname));

app.listen(PORT, () => {
  console.log(`FIX$ proxy server running at http://localhost:${PORT}`);
});
