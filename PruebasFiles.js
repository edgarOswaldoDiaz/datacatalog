const express = require('express');
const bodyParser = require('body-parser');
const mysql = require('mysql2');
const csv = require('csv-parser');
const csvWriter = require('csv-writer').createObjectCsvWriter;
const avro = require('avsc');
const sharp = require('sharp');
const parquet = require('parquetjs');
const { exec } = require('child_process');
const ffmpeg = require('fluent-ffmpeg');
const path = require('path');
const { PDFDocument } = require('pdf-lib');
const fs = require('fs');
const geojson = require('geojson');
const axios = require('axios');

app.use(bodyParser.json());
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

// Ruta para obtener todos los datos de la tabla test_table
app.get('/data', (req, res) => {
  let sql = 'SELECT * FROM test_table';
  db.query(sql, (err, results) => {
    if (err) throw err;
    res.json(results);
  });
});

// Ruta para obtener un dato específico de la tabla test_table por ID
app.get('/data/:id', (req, res) => {
  const id = req.params.id;
  let sql = 'SELECT * FROM test_table WHERE id = ?';
  db.query(sql, [id], (err, results) => {
    if (err) throw err;
    if (results.length > 0) {
      res.json(results[0]);
    } else {
      res.status(404).send('Data not found');
    }
  });
});

// Ruta para leer datos desde la base de datos
app.get('/read-csv', (req, res) => {
  const query = 'SELECT * FROM csv'; // Cambia 'csv' por el nombre de tu tabla
  db.query(query, (error, results) => {
    if (error) {
      console.error('Error ejecutando la consulta:', error.stack);
      res.status(500).json({ error: 'Error al obtener datos de la base de datos' });
      return;
    }
    res.json(results);
  });
});

// Ruta para descargar datos como CSV filtrando por ID
app.get('/download-csv/:id', (req, res) => {
  const id = req.params.id;
  const query = 'SELECT * FROM csv WHERE id = ?'; // Ajustar el nombre de la tabla y la columna de ID
  db.query(query, [id], (error, results) => {
    if (error) {
      console.error('Error en la consulta:', error);
      return res.status(500).json({ error: 'Error al obtener datos de la base de datos' });
    }
    if (results.length === 0) {
      return res.status(404).json({ error: 'No se encontraron datos para el ID proporcionado' });
    }
    // Convertir resultados a CSV
    const csvData = results.map(row => Object.values(row).join(',')).join('\n');
    // Configurar encabezados de la respuesta para la descarga del archivo CSV
    res.setHeader('Content-Type', 'text/csv');
    res.setHeader('Content-Disposition', `attachment; filename=output_${id}.csv`);
    // Enviar CSV como respuesta
    res.send(csvData);
  });
});

// Ruta para leer datos desde la tabla json_data y enviar como JSON
app.get('/read-json', (req, res) => {
  db.query('SELECT * FROM json_data', (error, results) => {
    if (error) {
      console.error('Error en la consulta:', error);
      return res.status(500).json({ error: 'Error al obtener datos de la base de datos' });
    }
    res.json(results); // Enviar los resultados como JSON
  });
});

// Ruta para descargar datos JSON filtrando por ID
app.get('/download-json/:id', (req, res) => {
  const id = req.params.id;
  const query = 'SELECT * FROM json_data WHERE id = ?';
  db.query(query, [id], (error, results) => {
    if (error) {
      console.error('Error en la consulta:', error);
      return res.status(500).json({ error: 'Error al obtener datos de la base de datos' });
    }
    if (results.length === 0) {
      return res.status(404).json({ error: 'No se encontraron datos para el ID proporcionado' });
    }
    // Configurar encabezados para la descarga del archivo JSON
    res.setHeader('Content-Type', 'application/json');
    res.setHeader('Content-Disposition', `attachment; filename=data_${id}.json`);

    // Enviar el resultado como JSON
    res.json(results[0]);
  });
});

// Ruta para obtener todos los registros de parquet_data
app.get('/view-parquet-data', (req, res) => {
  const sql = 'SELECT * FROM parquet_data';
  db.query(sql, (err, results) => {
    if (err) {
      console.error('Error al obtener datos de Parquet desde la base de datos:', err);
      return res.status(500).send('Error al obtener datos de Parquet desde la base de datos.');
    }
    res.json(results); // Enviar los resultados como JSON
  });
});

// Ruta para descargar el archivo Parquet desde la base de datos
app.get('/download-parquet/:id', (req, res) => {
  const id = req.params.id;
  const sql = 'SELECT * FROM parquet_data WHERE id = ?'; // Consulta con parámetro
  db.query(sql, [id], (err, results) => {
    if (err) {
      console.error('Error al obtener datos de Parquet desde la base de datos:', err);
      return res.status(500).send('Error al obtener datos de Parquet desde la base de datos.');
    }
    // Debería haber exactamente un resultado debido a la consulta por ID
    const { filename, parquet_content } = results[0];
    // Configurar los headers para la descarga
    res.setHeader('Content-Disposition', `attachment; filename="${filename}"`);
    res.setHeader('Content-Type', 'application/octet-stream');
    // Enviar el contenido del archivo Parquet como respuesta
    res.send(parquet_content);
  });
});

// Ruta para obtener todos los registros de avro_data
app.get('/view-avro-data', (req, res) => {
  const sql = 'SELECT * FROM avro_data';
  db.query(sql, (err, results) => {
    if (err) {
      console.error('Error al obtener datos de Avro desde la base de datos:', err);
      return res.status(500).send('Error al obtener datos de Avro desde la base de datos.');
    }
    res.json(results); // Enviar los resultados como JSON
  });
});

// Ruta para leer y descargar archivo Avro filtrando por ID
app.get('/download-avro/:id', (req, res) => {
  const id = req.params.id;
  const sql = 'SELECT avro_content FROM avro_data WHERE id = ?'; // Consulta SQL para obtener solo el contenido Avro
  db.query(sql, [id], (err, results) => {
    if (err || results.length === 0) {
      console.error('Error al obtener datos de Avro desde la base de datos:', err);
      return res.status(500).send('Error al obtener datos de Avro desde la base de datos.');
    }
    // Obtener el contenido Avro desde la base de datos
    const avroBuffer = results[0].avro_content; // Asumiendo que el contenido Avro está en un campo 'avro_content'
    // Configurar encabezados para la descarga
    res.setHeader('Content-Disposition', `attachment; filename="output-${id}.avro"`);
    res.setHeader('Content-Type', 'application/octet-stream');
    // Enviar el contenido Avro como respuesta
    res.send(avroBuffer);
  });
});

// Ruta para obtener todas las imágenes
app.get('/imagenes', (req, res) => {
  let sql = 'SELECT id, nombre, descripcion FROM imagenes';
  db.query(sql, (err, results) => {
    if (err) throw err;
    res.json(results);
  });
});

//Ruta para descagar imagen por ID
app.get('/imagen/:id/descargar', (req, res) => {
  const id = req.params.id;
  const sql = 'SELECT * FROM imagenes WHERE id = ?';
  db.query(sql, [id], (err, results) => {
    if (err) {
      console.error('Error al obtener la imagen:', err);
      return res.status(500).send('Error al obtener la imagen.');
    }
    if (results.length === 0) {
      return res.status(404).send('Imagen no encontrada');
    }
    const imagen = results[0];
    const mimeType = 'image/jpeg'; // Cambiar según el tipo de imagen almacenado
    res.setHeader('Content-Disposition', `attachment; filename="${imagen.nombre}.jpeg"`);
    res.setHeader('Content-Type', mimeType);
    res.send(imagen.imagen);
  });
});

// Ruta para mostrar registros de audio_data
app.get('/show-audio-data', (req, res) => {
  const sql = 'SELECT * FROM audio_data';
  db.query(sql, (err, result) => {
      if (err) {
          res.status(500).json({ error: 'Error al obtener los registros de audio_data' });
          return;
      }
      // Envía los registros en formato JSON como respuesta
      res.json(result);
  });
});

// Rutas para manipulación de audio
// Configuración de multer para la carga de archivos
const storage = multer.diskStorage({
  destination: function (req, file, cb) {
    cb(null, 'uploads/');
  },
  filename: function (req, file, cb) {
    cb(null, file.originalname);
  }
});
const upload = multer({ storage: storage });

// Ruta de prueba
app.get('/', (req, res) => {
  res.send('API funcionando');
});

// Ruta para la carga y conversión de audio
app.post('/convert-audio', upload.single('audio'), (req, res) => {
  const filePath = path.join(__dirname, 'uploads', req.file.originalname);
  const outputFilePath = path.join(__dirname, 'uploads', 'output.wav');

  ffmpeg(filePath)
    .toFormat('wav')
    .save(outputFilePath)
    .on('end', () => {
      res.send('Audio convertido correctamente.');
    })
    .on('error', (err) => {
      console.error('Error al convertir audio:', err);
      res.status(500).send('Error al convertir audio.');
    });
});


// // Rutas para manipulación de video
// app.post('/convert-video', (req, res) => {
//   ffmpeg('input.mp4')
//     .toFormat('avi')
//     .save('output.avi')
//     .on('end', () => {
//       res.send('Video converted successfully.');
//     });
// });

// Ruta para obtener todos los registros de la tabla pdf_data
app.get('/pdf-data', (req, res) => {
  const sql = 'SELECT * FROM pdf_data';
  db.query(sql, (err, results) => {
    if (err) {
      console.error('Error al obtener los datos:', err);
      return res.status(500).send('Error al obtener los datos.');
    }
    res.json(results);
  });
});

//Descargar PDF por su ID
app.get('/download-pdf/:id', (req, res) => {
  const pdfId = req.params.id;
  const sql = 'SELECT filename, pdf_content FROM pdf_data WHERE id = ?';
  db.query(sql, [pdfId], (err, results) => {
      if (err) {
          console.error('Error al obtener datos de PDF desde la base de datos:', err);
          return res.status(500).send('Error al obtener datos de PDF desde la base de datos.');
      }
      if (results.length === 0) {
          return res.status(404).send('PDF no encontrado en la base de datos.');
      }
      const { filename, pdf_content: pdfContent } = results[0];
      // Configurar los headers para la descarga del PDF
      res.setHeader('Content-disposition', `attachment; filename=${filename}`);
      res.setHeader('Content-type', 'application/pdf');
      // Enviar el contenido del PDF como respuesta
      res.send(pdfContent);
  });
});


// Ruta GET para obtener datos de la tabla geo_data y convertirlos a GeoJSON
app.get('/geo-data', (req, res) => {
  const sql = 'SELECT * FROM geo_data';
  
  db.query(sql, (err, results) => {
    if (err) {
      console.error('Error al obtener los datos:', err);
      return res.status(500).send('Error al obtener los datos.');
    }
    // Convertir los resultados a GeoJSON
    const geoJsonFeatures = results.map(row => ({
      type: 'Feature',
      geometry: {
        type: 'Point',
        coordinates: [row.longitude, row.latitude]
      },
      properties: {
        id: row.id,
        name: row.name
      }
    }));
    // Crear un objeto GeoJSON completo con todos los features
    const geoJson = {
      type: 'FeatureCollection',
      features: geoJsonFeatures
    };
    // Enviar la respuesta como JSON con el GeoJSON generado
    res.json(geoJson);
  });
});

// Ruta GET para descargar un registro de la tabla geo_data por su ID en formato GeoJSON
app.get('/geo-data/:id/download', (req, res) => {
  const id = req.params.id;
  const sql = 'SELECT id, name, longitude, latitude FROM geo_data WHERE id = ?';

  db.query(sql, [id], (err, results) => {
    if (err) {
      console.error('Error al obtener los datos:', err);
      return res.status(500).send('Error al obtener los datos.');
    }

    if (results.length === 0) {
      return res.status(404).send('Registro no encontrado');
    }

    // Extraer el único registro encontrado
    const row = results[0];

    // Crear el objeto GeoJSON para el registro encontrado
    const geoJsonFeature = {
      type: 'Feature',
      geometry: {
        type: 'Point',
        coordinates: [row.longitude, row.latitude]
      },
      properties: {
        id: row.id,
        name: row.name
      }
    };

    // Crear el objeto GeoJSON completo con el único feature
    const geoJson = {
      type: 'FeatureCollection',
      features: [geoJsonFeature]
    };

    // Configurar los encabezados de respuesta para la descarga del archivo
    res.setHeader('Content-Disposition', `attachment; filename="geo_data_${id}.json"`);
    res.setHeader('Content-Type', 'application/json');
    res.json(geoJson); // Enviar el GeoJSON directamente como respuesta
  });
});

// Ruta GET para simular la conversión de TIFF a PNG
app.get('/convert-tiff/:id', (req, res) => {
  const id = req.params.id;
  const sql = 'SELECT filename, tiff_data, converted_png_data FROM tiff_data WHERE id = ?';

  db.query(sql, [id], (err, results) => {
    if (err) {
      console.error('Error al obtener los datos del TIFF:', err);
      return res.status(500).send('Error al obtener los datos del TIFF.');
    }

    if (results.length === 0) {
      return res.status(404).send('Registro de TIFF no encontrado');
    }

    const { filename, tiff_data, converted_png_data } = results[0];

    // Verificar si ya se ha convertido a PNG
    if (converted_png_data) {
      // Si ya existe la versión PNG, enviarla como respuesta
      res.setHeader('Content-Disposition', `attachment; filename="${filename}.png"`);
      res.setHeader('Content-Type', 'image/png'); // Tipo MIME para PNG
      res.send(converted_png_data);
    } else {
      // Simular la conversión de TIFF a PNG (aquí puedes agregar la lógica real de conversión si lo deseas)
      sharp(tiff_data)
        .toFormat('png')
        .toBuffer((err, pngBuffer) => {
          if (err) {
            console.error('Error al convertir TIFF a PNG:', err);
            return res.status(500).send('Error al convertir TIFF a PNG.');
          }
          // Actualizar la base de datos con los datos convertidos a PNG
          const updateSql = 'UPDATE tiff_data SET converted_png_data = ?, conversion_status = ? WHERE id = ?';
          const params = [pngBuffer, 'completed', id];
          db.query(updateSql, params, (err, updateResult) => {
            if (err) {
              console.error('Error al actualizar la conversión a PNG en la base de datos:', err);
              return res.status(500).send('Error al actualizar la conversión a PNG en la base de datos.');
            }
            // Configurar los encabezados de respuesta para descargar el PNG convertido
            res.setHeader('Content-Disposition', `attachment; filename="${filename}.png"`);
            res.setHeader('Content-Type', 'image/png'); // Tipo MIME para PNG
            res.send(pngBuffer); // Enviar el PNG convertido como respuesta
          });
        });
    }
  });
});

// Rutas para integración con Apache Atlas
const ATLAS_BASE_URL = 'http://localhost:21000/api/atlas/v2';

// Obtener detalles de una entidad en Atlas por su ID
app.get('/atlas/entity/:id', async (req, res) => {
  const entityId = req.params.id;
  try {
    const response = await axios.get(`${ATLAS_BASE_URL}/entity/guid/${entityId}`, {
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

// Obtener metadatos de una tabla en Amundsen por su ID
app.get('/amundsen/table_metadata/:id', async (req, res) => {
  const tableId = req.params.id;
  try {
    const response = await axios.get(`${AMUNDSEN_METADATA_URL}/metadata/v0/table`, {
      params: {
        key: tableId
      }
    });
    res.json(response.data);
  } catch (error) {
    res.status(500).send(error.message);
  }
});

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
