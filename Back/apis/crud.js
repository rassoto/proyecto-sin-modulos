const express = require('express');
const admin = require('../firebaseAdmin');
const verificarAutenticacion = require('../middlewares/verificarAutenticacion');

//iniciar la aplicacion usando express
const app = express();
app.use(express.json());

//configuramos el endpoint para mostrar todos los datos
app.get('/vehiculos', verificarAutenticacion, async (req, res) => {
    try {
        const data = await admin.firestore().collection('vehiculos').get();
        const vehiculos = [];
        data.forEach(doc => {
            vehiculos.push({ id: doc.id, ...doc.data() });
        });

        res.status(200).json(vehiculos);
    } catch (error) {
        res.status(500).send('Error al consultar los datos: ' + error.message);
    }
});

app.get('/vehiculos/:id', verificarAutenticacion, async (req, res) => {
    const vehiculoId = req.params.id;

    try {
        const vehiculoRef = admin.firestore().collection('vehiculos').doc(vehiculoId);
        const doc = await vehiculoRef.get();

        if (!doc.exists) {
            res.status(404).send('No se encontró el vehículo');
        } else {
            res.status(200).json({ id: doc.id, ...doc.data() });
        }
    } catch (error) {
        res.status(500).send('Error al consultar los datos: ' + error.message);
    }
});

//configuramos el endpoint para eliminar un vehículo
app.delete('/vehiculos/:id', verificarAutenticacion, async (req, res) => {
    const vehiculoId = req.params.id;

    try {
        const vehiculoRef = admin.firestore().collection('vehiculos').doc(vehiculoId);

        const doc = await vehiculoRef.get();
        
        if (!doc.exists) {
            res.status(404).send('No se encontró el vehículo');
        } else {
            await vehiculoRef.delete();
            res.status(200).send('Vehículo eliminado correctamente');
        }
    } catch (error) {
        res.status(500).send('Error al eliminar el vehículo: ' + error.message);
    }
});

//configuramos el endpoint para agregar un vehículo
app.post('/agregarVehiculos', verificarAutenticacion, async (req, res) => {
    try {
        const newVehiculo = req.body;
        const ref = await admin.firestore().collection('vehiculos').add(newVehiculo);
        res.status(201).send('Vehículo creado con ID: ' + ref.id);
    } catch (error) {
        res.status(500).send('Error al agregar el vehículo: ' + error.message);
    }
});

//configuramos el endpoint para actualizar un vehículo
app.put('/vehiculos/:id', verificarAutenticacion, async (req, res) => {
    const vehiculoId = req.params.id;
    const updateData = req.body; // los nuevos datos a actualizar

    try {
        const vehiculoRef = admin.firestore().collection('vehiculos').doc(vehiculoId);

        const doc = await vehiculoRef.get();
        if (!doc.exists) {
            return res.status(404).send('No se encontró el vehículo');
        }

        await vehiculoRef.update(updateData);
        res.status(200).send('Vehículo actualizado correctamente');
    } catch (error) {
        res.status(500).send('Error al actualizar el vehículo: ' + error.message);
    }
});

module.exports = app;