//codigo configurado podman y atlas y documentacion inegi
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
const axios = require('axios');
const multer = require('multer');
const upload = multer({ dest: 'uploads/' });

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

  await reader.close();
  res.json(results);
});

// Rutas para manipulación de Avro
const avroType = avro.Type.forSchema({
  type: 'record',
  fields: [{ name: 'name', type: 'string' }]
});

app.post('/write-avro', (req, res) => {
  const buf = avroType.toBuffer(req.body);
  fs.writeFileSync('output.avro', buf);
  res.send('Avro file written successfully.');
});

app.get('/read-avro', (req, res) => {
  const buf = fs.readFileSync('output.avro');
  const data = avroType.fromBuffer(buf);
  res.json(data);
});

// Rutas para manipulación de imágenes
app.post('/process-image', (req, res) => {
  sharp('input.jpg')
    .resize(200)
    .toFile('output.png', (err, info) => {
      if (err) throw err;
      res.send('Image processed successfully.');
    });
});

// Rutas para manipulación de audio
app.post('/convert-audio', upload.single('audio'), (req, res) => {
  const filePath = req.file.path;
  const outputFilePath = 'output.wav';

  ffmpeg(filePath)ae
    .toFormat('wav')
    .save(outputFilePath)
    .on('end', () => {
      res.send('Audio converted successfully.');
    })
    .on('error', (err) => {
      res.status(500).send('Audio conversion failed: ' + err.message);
    });
});

// Rutas para manipulación de video
app.post('/convert-video', (req, res) => {
  ffmpeg('input.mp4')
    .toFormat('avi')
    .save('output.avi')
    .on('end', () => {
      res.send('Video converted successfully.');
    });
});

// Rutas para manipulación de texto
app.post('/create-pdf', async (req, res) => {
  const pdfDoc = await PDFDocument.create();
  const page = pdfDoc.addPage([600, 400]);
  page.drawText('Hello, world!');
  const pdfBytes = await pdfDoc.save();
  fs.writeFileSync('output.pdf', pdfBytes);
  res.send('PDF created successfully.');
});

// Rutas para manipulación de GeoJSON
app.post('/convert-to-geojson', (req, res) => {
  const data = req.body; // Expects an array of objects with coordinates
  const geo = geojson.parse(data, { Point: ['coordinates[1]', 'coordinates[0]'] });
  res.json(geo);
});

// Rutas para manipulación de TIFF
app.post('/convert-tiff', (req, res) => {
  sharp('input.tiff')
    .toFile('output.png', (err, info) => {
      if (err) throw err;
      res.send('TIFF converted to PNG successfully.');
    });
});

// Rutas para integración con Apache Atlas
const ATLAS_BASE_URL = 'http://localhost:21000/api/atlas/v2';

app.get('/atlas/entities', async (req, res) => {
  try {
    const response = await axios.get(`${ATLAS_BASE_URL}/entity/bulk`, {
      auth: {
        username: 'admin',
        password: 'admin'
      }
    });
    res.json(response.data);
  } catch (error) {
    res.status(500).send(error.message);
  }
});

app.post('/atlas/entity', async (req, res) => {
  try {
    const response = await axios.post(`${ATLAS_BASE_URL}/entity`, req.body, {
      auth: {
        username: 'admin',
        password: 'admin'
      }
    });
    res.json(response.data);
  } catch (error) {
    res.status(500).send(error.message);
  }
});

// Rutas para integración con Amundsen (Search y Metadata)
const AMUNDSEN_SEARCH_URL = 'http://localhost:5001';
const AMUNDSEN_METADATA_URL = 'http://localhost:5002';

app.get('/amundsen/search', async (req, res) => {
  try {
    const response = await axios.get(`${AMUNDSEN_SEARCH_URL}/search/v0/table`, {
      params: {
        q: req.query.q
      }
    });
    res.json(response.data);
  } catch (error) {
    res.status(500).send(error.message);
  }
});

app.get('/amundsen/table_metadata', async (req, res) => {
  try {
    const response = await axios.get(`${AMUNDSEN_METADATA_URL}/metadata/v0/table`, {
      params: {
        key: req.query.key
      }
    });
    res.json(response.data);
  } catch (error) {
    res.status(500).send(error.message);
  }
});

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
