const express = require('express');

const app = express();
const PORT = 3000;

app.get('/api/external-data', (req, res) => {
  res.json({ message: 'You accessed the EXTERNAL CLOUD SERVICE (RBAC success).' });
});

app.listen(PORT, () => {
  console.log(`Cloud service running on port ${PORT}`);
});
