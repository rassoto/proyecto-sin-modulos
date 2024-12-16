const claveDeAutenticacion = 'm+rD%=&wH@EbLpg--bU$xa!KHr/jnl'; // Clave de autenticación

function verificarAutenticacion(req, res, next) {
    const claveIngresada = req.header('Clave-De-Autenticacion');

    if (!claveIngresada || claveIngresada !== claveDeAutenticacion) {
        return res.status(401).json({ mensaje: 'Acceso no autorizado. Clave de autenticación incorrecta.' });
    }
    // La autenticación es exitosa, permitir que la solicitud continúe
    next();
}

module.exports = verificarAutenticacion;