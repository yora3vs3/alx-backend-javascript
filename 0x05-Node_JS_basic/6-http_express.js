const express = require('express');

const app = express();
const port = 1245;

app.get('/', (_request, response) => {
  response.send('Hello Holberton School!');
});

app.listen(port, () => {
});

module.exports = app;
