const express = require('express');
const jwt = require('jsonwebtoken');

const app = express();
const PORT = 3000;

app.get('/api/external', (req, res) => {
  const authHeader = req.headers['authorization'];
  const token = authHeader && authHeader.split(' ')[1];

  if (!token) return res.status(401).send('Unauthorized');

  try {
    const decoded = jwt.decode(token); // Decode JWT for demo purposes
    res.json({ message: `Hello ${decoded.preferred_username}, you accessed the external service!` });
  } catch (err) {
    res.status(403).send('Invalid token');
  }
});

app.listen(PORT, () => {
  console.log(`Cloud service running on port ${PORT}`);
});
