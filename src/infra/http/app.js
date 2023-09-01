const express = require('express');

const app = express();
const port = Number(process.env.PORT || 3000);

app.listen(port, () => {
  console.info(`Server running on port ${port}`);
});
