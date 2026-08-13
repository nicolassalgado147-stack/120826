const express = require('express');
const mysql = require('mysql2');
const app = express();
const port = 5050;

// Configuración de la conexión a MySQL
const db = mysql.createConnection({
    host: process.env.DB_HOST || 'db',
    user: process.env.DB_USER || 'root',
    password: process.env.DB_PASSWORD || 'root',
    database: process.env.DB_NAME || 'adso_db'
});

// Ruta principal que exige la asignación
app.get('/', (req, res) => {
    res.send('Conexión exitosa a la base de datos');
});

app.listen(port, () => {
    console.log(`Servidor Node.js corriendo en el puerto ${port}`);
});