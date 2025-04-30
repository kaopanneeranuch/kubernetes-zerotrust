const express = require('express');
const jwt = require('jsonwebtoken');
const axios = require('axios');

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware to check JWT in Authorization header
app.use((req, res, next) => {
  const authHeader = req.headers['authorization'];
  const token = authHeader && authHeader.split(' ')[1];

  if (!token) return res.status(401).send('Token missing');

  try {
    const decoded = jwt.decode(token); // You can use jwt.verify() for actual validation
    req.user = decoded; // Store user info
    next();
  } catch (err) {
    res.status(401).send('Invalid token');
  }
});

// Sample route to call API 1
app.get('/data', async (req, res) => {
  try {
    const api1Response = await axios.get('http://internal-api-1.default.svc.cluster.local/api/data', {
      headers: { Authorization: `Bearer ${req.headers.authorization}` }
    });
    res.json(api1Response.data);
  } catch (err) {
    res.status(500).send('Error calling internal API 1');
  }
});

app.listen(PORT, () => {
  console.log(`Frontend Service running on port ${PORT}`);
});
