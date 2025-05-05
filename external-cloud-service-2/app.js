const express = require('express');

const app = express();
const PORT = 3001;

app.get('/api/external-report', (req, res) => {
  res.json({ message: 'You accessed the SECURE REPORT in Cloud Service 2.' });
});

app.listen(PORT, () => {
  console.log(`Cloud Service 2 running on port ${PORT}`);
});
