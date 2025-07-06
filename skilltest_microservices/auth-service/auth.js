const express = require('express');
const app = express();
const PORT = 4000;

app.get('/', (req, res) => {
  res.send('Auth Service is running');
});

app.listen(PORT, () => console.log(`Auth service running on port ${PORT}`));
