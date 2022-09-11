const express = require('express');
app = express();

port = process.env.PORT || 3000;

app.use(express.static('.'));
app.use(express.static('src'));

app.listen(port);