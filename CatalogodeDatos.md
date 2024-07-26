Índex
INTEGRANTES:	1
ASESOR:	1
LABORATORIO DE CIENCIA DE DATOS	1
Introducción sobre el Catálogo de Datos	4
Metodología	4
Características	5
Recomendaciones Futuras	6
Requerimientos de instalación	7
Instalación de Postman	7
Instalación de docker	10
Instalación de wls2	14
Contendores postman api configuración	16
Codigo:	17
Descripción del código	21
Continuación de configuración de contenedores api	21
pruebas de contenedor	23
Solicitudes en Postman	23
1. Leer CSV:	23
2.  Escribir CSV:	23
3. Leer JSON:	24
4.  Escribir JSON:	25
5.  Leer Parquet:	26
6.  Escribir Avro:	26
7.  Leer Avro:	26
8.  Procesar Imagen:	27
9.  Convertir Audio:	27
10.  Convertir Video:	28
11.  Crear PDF:	28
12.  Convertir a GeoJSON:	28
13.  Convertir TIFF:	29
Instalación de podman	30
Instalación PostgreSQL	35
Migrar base de datos de MySQL a PostgreSQL usando DM Toolkit	57
Contenedores en Docker	65
Instalación de contenedores	65
Ejecución de los contenedores ya corriendo	66
Conclusiones	68
Conclusión General	69
Competencias desarrolladas y/o aplicada	70
Referencias	75

## Introducción sobre el Catálogo de Datos
En el mundo moderno de la ciencia de datos, la gestión y el análisis eficiente de grandes volúmenes de datos son fundamentales para extraer valor y conocimiento. Un lago de datos (Data Lake) es una arquitectura que permite almacenar datos en su forma nativa, sin procesar, desde una variedad de fuentes. La diversidad y el volumen de datos almacenados en un lago de datos pueden presentar desafíos significativos en términos de organización y accesibilidad.
El objetivo principal de este proyecto es llevar a cabo una revisión exhaustiva del lago de datos existente para comprender y documentar los diferentes tipos de conjuntos de datos disponibles. Este proceso incluye la identificación de esquemas, estructuras y relaciones entre los datos, así como la utilización de herramientas automatizadas para acelerar la catalogación. La meta final es organizar toda la información en un catálogo estructurado y fácilmente accesible, que sirva como una herramienta valiosa para ingenieros y científicos de datos.

### Metodología
El proceso de catalogación se dividió en varias etapas clave:
1.	Preparativos e Instalaciones:
•	Configuración de un entorno de trabajo utilizando Docker y WSL2.
•	Instalación de una base de datos opcional para almacenar la catalogación.
2.	Exploración de Datos:
•	Uso de Jupyter Lab y bibliotecas como pandas para la exploración inicial de los datos.
•	Identificación de características clave de los datos, como el esquema, formato, tamaño y descripción del contenido.
3.	Automatización del Proceso de Catalogación:
•	Desarrollo de scripts automatizados para explorar y catalogar los conjuntos de datos.
•	Generación de un archivo consolidado que documenta los detalles de cada conjunto de datos.
4.	Verificación y Documentación:
•	Realización de pruebas aleatorias y/o cruzadas para verificar la precisión y exhaustividad de la catalogación.
•	Documentación detallada de cada conjunto de datos, incluyendo su origen, formato, tamaño y descripción general del contenido.
5.	Presentación y Revisión:
•	Presentación del catálogo final mediante videoconferencia para obtener comentarios y realizar las correcciones necesarias.
•	Generación de un archivo digital (.xlsx o .csv) con la información detallada de cada conjunto de datos y una presentación breve que explique los hallazgos.

### Características

Eficiencia y Organización:
1.	La implementación de herramientas automatizadas para la catalogación de datos ha demostrado ser altamente eficiente, permitiendo una organización rápida y precisa de grandes volúmenes de datos. Este enfoque ha facilitado la creación de un catálogo estructurado y accesible que mejora significativamente la capacidad de los científicos e ingenieros de datos para encontrar y utilizar los conjuntos de datos necesarios.
Precisión y Exhaustividad:
2.	Las pruebas de verificación han confirmado la precisión y exhaustividad del catálogo de datos, asegurando que todos los conjuntos de datos están correctamente documentados. Esto proporciona una base confiable para futuras investigaciones y análisis, minimizando el riesgo de errores y omisiones.
Colaboración y Mejora Continua:
3.	La presentación del catálogo y la incorporación de comentarios de los usuarios han sido cruciales para refinar y mejorar la documentación. Este proceso colaborativo ha permitido identificar áreas de mejora y ha asegurado que el catálogo final sea lo más útil y preciso posible.
Facilidad de Acceso y Uso:
4.	La organización de la información en un formato digital accesible (.xlsx o .csv) facilita su uso y consulta por parte de los interesados. La presentación complementaria ayuda a contextualizar los datos y a explicar los hallazgos de manera clara y concisa.

### Recomendaciones Futuras
Actualización Continua:
1.	Se recomienda mantener el catálogo de datos actualizado con cualquier nuevo conjunto de datos que se agregue al lago. Esto puede lograrse mediante la implementación de scripts automatizados que monitoricen y actualicen el catálogo de manera regular.
Capacitación y Documentación:
2.	Proveer capacitación continua para los usuarios del catálogo y mantener una documentación clara y accesible sobre el proceso de catalogación y las herramientas utilizadas.
Evaluación Periódica:
3.	Realizar evaluaciones periódicas del catálogo y del proceso de catalogación para identificar posibles mejoras y asegurar que las mejores prácticas se sigan implementando.
Escalabilidad:
4.	Considerar la escalabilidad del sistema para manejar volúmenes crecientes de datos y la integración de nuevas herramientas y tecnologías que puedan surgir en el futuro.
La creación y el mantenimiento de un catálogo de datos eficiente son cruciales para maximizar el valor del lago de datos y apoyar el trabajo de los científicos e ingenieros de datos en la organización.


## Requerimientos de instalación


### Instalación de Postman
 
En el navegador buscamos postman, seleccionamos la segunda opción para descargar que será Download Postman.

 
Ingresado a la página de postman, descargamos para Windows 64-bit que en este caso fue nuestra arquitectura de computadora en caso de ser de 32 bits descargar de 32 bits.

  
Antes de continuar, pedirá que se ingrese un correo electrónico. En este caso creamos una cuenta nueva.

 

Es necesario llenar el formulario con los datos solicitados.

 

Una vez llenado los campos tenemos nuestra cuenta creada, abrimos postman.

 Es 
importante que le asignemos un nombre de usuario y un rol. 



### Instalación de docker

buscaremos lo que es docker, ingresaremos al link que dice docker desktop, que sería docker escritorio.
  
 
A continuación, en la página seleccionaremos lo que es download for Windows esto teniendo en cuenta que nosotros estamos utilizando Windows con la virtualización WSL2.
  
 
Una vez descargado le daremos click izquierdo y ejecutar como administrador para no tener problemas con los permisos y nos pueda correr normalmente como debería.
 
  
Aquí cómo podemos ver seleccionamos las 2 opciones habrá a veces que nos aparezca la primera opción dependiendo cómo tengamos la instalación de WLS 2 y habrá veces que no nos aparezca igual de cualquiera de las 2:00 maneras que no nos aparece no hay problema y si nos aparecen no nos aparece seleccionar la casilla y hacer la instalación donde daremos okey y automáticamente comenzará a instalarse por sí solo, descargar lo que se necesita y se configurará automáticamente poniéndonos también lo que es un acceso directo.
  
 
 

Aquí como podemos ver ya tenemos lo que es configurado docker para poder hacer nuestras prácticas con los contenedores que se nos requirieron, hoy en caso de que nos llegue a marcar error solamente ejecutamos la aplicación como administrador y nos agregaría ya que es muy común este error cuando se tiene instalado en caso de no tenerse la aplicación correrá normalmente como debería hacerlo.
 
  

### Instalación de wls2


Buscamos activar o desactivar características de Windows hoy damos enter.
  
 
Nos abrirá una pestaña con varias opciones y seleccionaremos las siguientes que será subsistema de Windows para linux, virtual machin plataforma, esto para poder activar lo que es ubuntu en nuestra computadora sin necesidad de descargar máquina virtual.
  
 
Después buscaremos en el buscador de nuestra computadora la tienda oficial de Microsoft store y daremos enter y nos abrirá la siguiente ventana.
  
 
Descargaremos e instalaremos ubuntu para poder hacer las pruebas necesarias con todos los contenedores qué requerimos.
  
Estos serán todos los pasos para instalar wls2 para poder hacer todas nuestras pruebas.


## Contendores postman api configuración

1. Creamos un proyecto en Node.js
•	Abrimos la una terminal con la ruta donde deseamos crear nuestro en la ubicación que gustemos y corremos los siguientes comandos:

mkdir api-server
cd api-server

•	Ahora inicializaremos nuestro proyecto corriendo el siguiente comando en la ruta de dicho proyecto o terminal:

npm init -y
 
2. Instalar Express
•	Instalaremos Express junto con sus paquetes necesarios con el siguiente comando:

npm install express body-parser mysql2

 
2.	Ahora crearemos un archivo llamado server.js en el directorio de nuestro proyecto y en el archivo pondremos el siguiente código:

### Codigo:
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
app.post('/convert-audio', (req, res) => {
  ffmpeg('input.mp3')
    .toFormat('wav')
    .save('output.wav')
    .on('end', () => {
      res.send('Audio converted successfully.');
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

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));


#### Descripción del código
Este código es una aplicación de Express.js en Node.js que proporciona una API con varias rutas para manipular diferentes tipos de datos, incluyendo bases de datos MySQL, archivos CSV, JSON, Parquet, Avro, imágenes, audio, video, PDF y GeoJSON. Aquí está la descripción detallada de cada parte del código.
esta aplicación proporciona una serie de rutas para manipular diferentes tipos de archivos y datos, permitiendo realizar operaciones como leer, escribir, convertir y procesar información de manera sencilla y directa a través de una API RESTful.

### Continuación de configuración de contenedores api

4. Ahora instalamos las siguientes librerías para los tipos de archivos que va a usar el contenedor con los siguientes comandos:
npm install csv-parser csv-writer parquetjs avsc sharp fluent-ffmpeg pdf-lib html-pdf winston shapefile geojson
 



npm install parquetjs-lite
 

5. Iniciar los servicios de Apache y MySQL:
•	Abrimos el Panel de Control de XAMPP.
•	Iniciamos los módulos de Apache y MySQL haciendo clic en "Start" junto a cada uno.
6.  Configurar MySQL en XAMPP:
•	Abre phpMyAdmin desde el Panel de Control de XAMPP o navegando a http://localhost/phpmyadmin en tu navegador.
•	Crea una base de datos nueva llamada testdb.
•	En la base de datos testdb, crea una tabla test_table con las columnas necesarias.

CREATE TABLE test_table (
  id INT AUTO_INCREMENT,
  name VARCHAR(255),
  PRIMARY KEY (id)
);
INSERT INTO test_table (name) VALUES ('Test Data');

7. Iniciamos nuestro servidor con el siguiente comando:
node server.js
 



## pruebas de contenedor

### Solicitudes en Postman
#### 1. Leer CSV:
•	Método: GET
•	URL: http://localhost:5000/read-csv
•	Haz clic en "Send" para enviar la solicitud.
•	Deberías ver los datos del archivo CSV como respuesta.
 
#### 2.  Escribir CSV:
•	Método: POST
•	URL: http://localhost:5000/write-csv
•	En la pestaña "Body", selecciona "raw" y elige "JSON" como tipo de dato.
•	Agrega un JSON como el siguiente:
json
Copiar código
[
  { "name": "Miguel", "age": 78 }
]
•	Haz clic en "Send" para enviar la solicitud.
•	Deberías ver un mensaje indicando que el archivo CSV se ha escrito correctamente.
 
 
#### 3. Leer JSON:
•	Método: GET
•	URL: http://localhost:5000/read-json
•	Haz clic en "Send" para enviar la solicitud.
•	Deberías ver el contenido del archivo JSON.
 
#### 4.  Escribir JSON:
•	Método: POST
•	URL: http://localhost:5000/write-json
•	En la pestaña "Body", selecciona "raw" y elige "JSON" como tipo de dato.
•	Agrega un JSON como el siguiente:
json
Copiar código
{ "message": "Hello, JSON!" }
•	Haz clic en "Send" para enviar la solicitud.
•	Deberías ver un mensaje indicando que el archivo JSON se ha escrito correctamente.
