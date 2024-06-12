const express = require('express');
const bodyParser = require('body-parser');
const mysql = require('mysql2');
const csv = require('csv-parser');
const csvWriter = require('csv-writer').createObjectCsvWriter;
const parquet = require('parquetjs-lite');
const avro = require('avsc');
const sharp = require('sharp');
const ffmpeg = require('fluent-ffmpeg');
const { PDFDocument } = require('pdf-lib');
const fs = require('fs');
const geojson = require('geojson');

const app = express();
app.use(bodyParser.json());

// Configurar conexión a la base de datos MySQL
const db = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: '',
  database: 'testdb'
});

db.connect((err) => {
  if (err) {
    throw err;
  }
  console.log('MySQL Connected...');
});

// Ruta de prueba
app.get('/', (req, res) => {
  res.send('API funcionando');
});

// Ruta para obtener datos
app.get('/data', (req, res) => {
  let sql = 'SELECT * FROM test_table';
  db.query(sql, (err, results) => {
    if (err) throw err;
    res.json(results);
  });
});

// Rutas para manipulación de CSV
app.get('/read-csv', (req, res) => {
  let results = [];
  fs.createReadStream('data.csv') // Asegúrate de que 'data.csv' está en el directorio correcto
    .pipe(csv())
    .on('data', (data) => results.push(data))
    .on('end', () => {
      res.json(results);
    });
});

app.post('/write-csv', (req, res) => {
  const writer = csvWriter({
    path: 'output.csv',
    header: [
      { id: 'name', title: 'NAME' },
      { id: 'age', title: 'AGE' }
    ]
  });

  writer.writeRecords(req.body)
    .then(() => res.send('CSV file written successfully.'));
});

// Rutas para manipulación de JSON
app.get('/read-json', (req, res) => {
  const data = require('./data.json');
  res.json(data);
});

app.post('/write-json', (req, res) => {
  fs.writeFileSync('output.json', JSON.stringify(req.body, null, 2));
  res.send('JSON file written successfully.');
});

// Ruta para leer Parquet
app.get('/read-parquet', async (req, res) => {
  let reader = await parquet.ParquetReader.openFile('data.parquet');
  let cursor = reader.getCursor();
  let record = null;
  let results = [];

  while (record = await cursor.next()) {
    results.push(record);
  }