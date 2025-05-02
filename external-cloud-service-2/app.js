const express = require('express');

const app = express();
const PORT = 3000;

app.get('/api/secure-report', (req, res) => {
  res.json({ message: 'You accessed the SECURE REPORT in Cloud Service 2 (RBAC success).' });
});

app.listen(PORT, () => {
  console.log(`Cloud Service 2 running on port ${PORT}`);
});
