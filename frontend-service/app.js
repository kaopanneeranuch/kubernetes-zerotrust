const express = require('express');
const axios = require('axios');

const app = express();
const PORT = process.env.PORT || 3000;

// Route to call API 1
app.get('/data', async (req, res) => {
  try {
    const response = await axios.get('http://internal-api-1.default.svc.cluster.local/api/data', {
      headers: { Authorization: req.headers.authorization }
    });
    res.json(response.data);
  } catch (err) {
    res.status(err.response?.status || 500).send(err.response?.data || 'Error calling internal API 1');
  }
});

// Route to call API 2
app.get('/report', async (req, res) => {
  try {
    const response = await axios.get('http://internal-api-2.default.svc.cluster.local/api/report', {
      headers: { Authorization: req.headers.authorization }
    });
    res.json(response.data);
  } catch (err) {
    res.status(err.response?.status || 500).send(err.response?.data || 'Error calling internal API 2');
  }
});

app.listen(PORT, () => {
  console.log(`Frontend Service running on port ${PORT}`);
});
