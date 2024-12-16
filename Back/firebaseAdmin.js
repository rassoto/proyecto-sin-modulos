const admin = require('firebase-admin');


if(!admin.apps.length){
    const serviceAccount = require('./serviceAccountKey.json');
    admin.initializeApp({
        credential: admin.credential.cert(serviceAccount),
        databaseURL: 'https://gestortallerautomotriz.firebaseio.com'
    });
}


module.exports = admin;