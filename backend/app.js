const express = require('express');
const app = express();
const PORT = 5000;

app.get('/', (req, res) => {
  res.send('Backend Service is running');
});

app.listen(PORT, () => console.log(`Backend running on port ${PORT}`));

