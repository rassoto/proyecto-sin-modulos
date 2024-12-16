const express = require('express');
const punycode = require('punycode');
const verificarAutenticacion = require('./middlewares/verificarAutenticacion');


//defino Rutas
const app = require('./apis/crud');

//verifico tokens
app.use(verificarAutenticacion);



app.listen(3000, () => {
    console.log('Servidor iniciado en puerto 3000');
});

