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

 
#### 5.  Leer Parquet:
•	Método: GET
•	URL: http://localhost:5000/read-parquet
•	Haz clic en "Send" para enviar la solicitud.
•	Deberías ver los datos del archivo Parquet.
#### 6.  Escribir Avro:
•	Método: POST
•	URL: http://localhost:5000/write-avro
•	En la pestaña "Body", selecciona "raw" y elige "JSON" como tipo de dato.
•	Agrega un JSON como el siguiente:
json
Copiar código
{ "name": "Alice" }
•	Haz clic en "Send" para enviar la solicitud.
•	Deberías ver un mensaje indicando que el archivo Avro se ha escrito correctamente.
#### 7.  Leer Avro:
•	Método: GET
•	URL: http://localhost:5000/read-avro
•	Haz clic en "Send" para enviar la solicitud.
•	Deberías ver el contenido del archivo Avro.
#### 8.  Procesar Imagen:
•	Método: POST
•	URL: http://localhost:5000/process-image
•	Haz clic en "Send" para enviar la solicitud.
•	Deberías ver un mensaje indicando que la imagen se ha procesado correctamente.
 
 
#### 9.  Convertir Audio:
•	Método: POST
•	URL: http://localhost:5000/convert-audio
•	Haz clic en "Send" para enviar la solicitud.
•	Deberías ver un mensaje indicando que el audio se ha convertido correctamente.
#### 10.  Convertir Video:
•	Método: POST
•	URL: http://localhost:5000/convert-video
•	Haz clic en "Send" para enviar la solicitud.
•	Deberías ver un mensaje indicando que el video se ha convertido correctamente.
#### 11.  Crear PDF:
•	Método: POST
•	URL: http://localhost:5000/create-pdf
•	Haz clic en "Send" para enviar la solicitud.
•	Deberías ver un mensaje indicando que el PDF se ha creado correctamente.
 
#### 12.  Convertir a GeoJSON:
•	Método: POST
•	URL: http://localhost:5000/convert-to-geojson
•	En la pestaña "Body", selecciona "raw" y elige "JSON" como tipo de dato.
•	Agrega un JSON como el siguiente:
json
Copiar código
[
  { "name": "Dinagat Islands", "coordinates": [125.592, 10.05] }
]
•	Haz clic en "Send" para enviar la solicitud.
•	Deberías ver el contenido del archivo GeoJSON.
#### 13.  Convertir TIFF:
•	Método: POST
•	URL: http://localhost:5000/convert-tiff
•	Haz clic en "Send" para enviar la solicitud.
•	Deberías ver un mensaje indicando que el TIFF se ha convertido correctamente.


### Instalación de podman
Podman Desktop es una herramienta de software la cual permite gestionar contenedores facilitando el desarrollo de aplicaciones en un entorno local.
En este caso esta herramienta es de utilidad para hacer uso de los contenedores para las herramientas de nuestro catálogo de datos
Para realizar la instalación de este software abriremos una consola en powershell como administrador y escribiremos el siguiente comando:  winget install – e –id RedHat.Podman-Desktop

 

Posteriormente configuraremos podman para que pueda funcionar con los contenedores para esto click en initialize and start para inicializar el servicio de podman
 

Unos momentos después nos preguntara si queremos que el servicio de podman inicie automáticamente al iniciar la aplicación, click en next

 

Ahora nos pedirá crear una máquina de podman por lo que procederemos a crear una clickeando en next para crear una

 

Posteriormente a eso el servicio de podman estará inicializado correctamente

 
Una vez este inicializado el servicio de podman, procederemos a obtener las imágenes de los contenedores mediante el comando podman pull *nombre del contenedor en dockerhub*
En este caso se descarga el contenedor de apache atlas


Y realizaremos el mismo proceso para el resto de los contenedores a utilizar

 

Una vez descargadas la imagen click el icono de Play y procederemos a configurar e inicializar el contenedor correspondiente de cada imagen

 

Una vez le demos a Start Container el contenedor comenzará a ejecutarse y estará listo para ser utilizado


### Instalación PostgreSQL

 

Accedemos a la página oficial PostgreSQL https://www.postgresql.org/download/. Muestra las opciones de descarga, a nosotros nos interesa descargar para el sistema operativo Windows.
 
 

En esta página nos muestra el instalador y certificado por EDB para PostgreSQL que incluye el servidor PostgreSQL, pgAdmin (una herramienta gráfica para la gestión de bases de datos) y StackBuilder (un gestor de paquetes para descargar e instalar herramientas y controladores adicionales de PostgreSQL). Este instalador ofrece modos de instalación gráfica o silenciosa y está diseñado para facilitar y agilizar el proceso de configuración de PostgreSQL en Windows. Damos clic en download the installer. 

 

Tenemos la página donde vemos los diferentes sistemas operativos para realizar la descarga y al igual tenemos la versión del PostgreSQL. Nos interesa descargar para el sistema operativo de Windows con la arquitectura de x86-64 bits. Descargamos la última versión “16.3”. 
 

Una vez descargado el instalador lo ejecutamos, abrirá la siguiente venta como se muestra en la imagen. Nos dará la bienvenida a la instalación, solo le damos siguiente. 
 

El siguiente paso será asignar la dirección de instalación de PostgreSQL. Lo dejamos por default. 


Se deberá elegir los componentes que deseamos instalar. 


Seleccionamos todos los componentes para y continuamos con la instalación.  
 

Nuevamente nos dará la opción de seleccionar un directorio donde se almacenará los datos de la instalación. Lo dejamos por default, ya que esto se almacenará en la ruta ya asignada. 
 

Pedirá que ingresemos una contraseña para el superusuario para hacer uso de las bases de datos.  
 

Se deberá asignar un puerto para el servidor. Igual lo dejamos por default. 
 

Seleccionamos la configuración regional para usar el closter de la base de datos. Lo ponemos español México. 
 

Si estamos seguros de las configuraciones, procedemos a darle siguiente para que comience la instalacion.
 

La instalación comenzara y esperamos a que finalice. 
 

Una vez finalizado la instalación, preguntar a si deseamos instalar herramientas adicionales, le dejamos marcado la casilla especificando una respuesta positiva y le damos terminar 

Nuevamente abrirá una ventana, el cual es para continuar con la instalación de PostgreSQL, solo que ahora será para la instalación de herramientas y componentes. Además, señala la configuración que se tiene, el servidor llamado PostgreSQL 16 con el puerto que escuchara para la conexión. 
 

Ahora elegimos las herramientas a utilizar. En database drivers seleccionamos todos y en database server elegimos postgresql con la versión que se instaló. En este caso sería la versión 16.
 

Esperamos que empiece la instalación. 
 

Si estamos seguros podemos iniciar con la instalación. 
 

Empezara a instalar la primera herramienta llamada Npsgql. 


Señalamos el directorio donde se guardará la instalación de la herramienta. Lo dejamos por default. 
 

Nos muestra que un mensaje que la configuración esta lista para comenzar la instalación del componente. Le damos siguiente. 
 

Esperamos a que finalice la instalación. 
 

Sea ha completado la descarga. De esa misma manera hacemos con las demás herramientas. 
 

Descargado las herramientas, una vez más señala la instalación de postgresql. 

 

Nos dice que termino la instalación correctamente. 

 

Para completar la instalación debemos de reiniciar la pc. Lo realizamos. 
 

Ya que haya reiniciado la pc, abrimos el software pg Admin.

 

En funcionamiento, para conectarnos al servidor de PostgreSQL es necesario ingresar la contraseña que elegimos. Tenemos la opción que guarde la contraseña por si queremos conectarnos al servidor sin necesidad que la pida. 
 

Ingresado la contraseña ya está en funcionamiento posgreSQL.  

#### Migrar base de datos de MySQL a PostgreSQL usando DM Toolkit

 

En nuestro navegador buscamos la herramienta Data Migration Toolkit. Este software facilita la transferencia de datos entre diferentes sistemas o aplicaciones. Ayuda a mapear, transformar y migrar datos con precisión, minimizando riesgos y errores durante el proceso. Es útil para actualizar sistemas, consolidar datos o moverlos a nuevas plataformas, asegurando integridad y consistencia de los datos trasladados. Accedemos a la segunda opción para descargar. 

 

Estando en el sitio web de descargar de DMToolkit. Descargamos “DMTooltik_x64.zip” ya que depende de la arquitectura de nuestra PC, en este caso nuestra computadora nuestro sistema es de 64. 

 

Prendemos los servicios de apache y MySQL. 

 

Una vez descargado el software, extraído y ponerlo en ejecución, abrirá la siguiente venta. El cual, debemos de seleccionar la extensión que tiene nuestra base de datos que deseamos migrar. Convertiremos de MySQL a PostgreSQL, en el server dejamos por default como localhost y el puerto como 3306. Ahora seleccionamos la base de datos a migrar. 
  

En el destino colocamos a la base de datos que migraremos, seria PostgreSQL. En server, port y usename lo dejamos por default. Solo es necesario colocar nuestra contraseña de PostgreSQL y asígnale un nombre a nuestra base de datos. La llamaremos “testdb”.


 

Una vez completado los pasos anteriores mostrara una lista de las tablas que contiene la base de datos a migrar, podemos elegir la que nos interesa cambiar, pero, nosotros migraremos todo el contenido. Le damos siguiente. 
 

Comenzará el proceso de convertimiento, esto puede tardar de acuerdo al peso que tenga la base de datos. 

 


Ya que haya finalizado el proceso de convertimiento, en nuestro postgreSQL podemos observar que, en el apartado de base de datos en el menú izquierdo, observamos que tenemos nuestra base de datos migrada. Para ello hacemos una pequeña consulta solo para confirmar que funciona correctamente. Obtenemos los registros de nuestra tabla csv.

 

Para exportar nuestra base de datos, seleccionamos la base de datos llamada “testdb”, damos clic derecho y se abrirá una ventana con varias opciones, seleccionamos “backup”.
 
Se abrirá otra ventana, en la cual debemos solo asignar la ruta en donde se guardará la base de datos. También asignamos un nombre. Otra cosa importa es seleccionar el formato, escogemos “custom”, ya que esta es ideal para respaldos completos que incluyen tanto datos como la estructura de la base de datos. Es comprimido y más eficiente. Le damos clic en backup. 

 

Cuando termine de exportarse la base de datos, mostrara que el proceso fue exitoso y nos da la opción de ver el proceso. 


## Contenedores en Docker 
### Instalación de contenedores 
Comando: docker pull opnmetadata/docs

 
Descarga la imagen openmetadata/docs desde el registro de Docker Hub a tu máquina local, permitiéndote luego crear contenedores basados en esta imagen. Esto es útil para preparar el entorno antes de ejecutar un contenedor específico, asegurando que tienes la última versión de la imagen disponible.

Comando: docker pull openmetadata/ingestión

 
 
descarga la imagen openmetadata/ingestion desde el registro de Docker Hub a tu máquina local, permitiéndote luego crear contenedores basados en esta imagen. Esto es útil para preparar el entorno antes de ejecutar un contenedor específico, asegurando que tienes la última versión de la imagen disponible.

Comando: docker pull openmetadata/server

 
Descarga la imagen openmetadata/server desde el registro de Docker Hub a tu máquina local, permitiéndote luego crear contenedores basados en esta imagen. Esto es útil para preparar el entorno antes de ejecutar un contenedor específico, asegurando que tienes la última versión de la imagen disponible.

## Ejecución de los contenedores ya corriendo
Comando: 

docker run -d -p 80:80 -e OPENMETADATA_DB_HOST=your_db_host -e OPENMETADATA_DB_USER=your_db_user -e OPENMETADATA_DB_PASSWORD=your_db_password openmetadata/ingestion webserver

 
Este comando configura y ejecuta un servidor web de OpenMetadata dentro de un contenedor Docker, asegurando que esté correctamente conectado a una base de datos externa y accesible a través del puerto 80.


Comando:

docker ps -a

 
Es esencial para la administración de contenedores Docker, ya que te proporciona una visión completa de todos los contenedores, permitiéndote gestionar su estado y realizar las acciones necesarias en función de su estado actual y su historial.

Comando:

docker run -d -p 80:80 opnmetadata/server

 
Configura y ejecuta un servidor web de OpenMetadata dentro de un contenedor Docker, asegurando que esté accesible a través del puerto 80 del host y que se ejecute en segundo plano para no bloquear la terminal del usuario.

## Conclusiones
Ernesto Yael Ponce Gómez

Mi experiencia fue en la instalación y configuración de las herramientas esenciales para el proyecto, incluyendo Docker y WSL2. Su enfoque meticuloso en la preparación del entorno de trabajo garantizó una base sólida para el desarrollo y ejecución del catálogo de datos. Además, su habilidad para solucionar problemas técnicos rápidamente fue fundamental para superar obstáculos durante la implementación de contenedores y la configuración de bases de datos.

Lauro Manuel Cárdenas Herrera

Mi experiencia fue en la automatización del proceso de catalogación de datos, desarrollando scripts que facilitaron la exploración y documentación de diversos conjuntos de datos. Su expertise en el uso de Jupyter Lab y bibliotecas como pandas permitió identificar y catalogar eficientemente las características clave de los datos, mejorando significativamente la precisión y exhaustividad del catálogo final. Su capacidad para integrar comentarios de usuarios y realizar ajustes en tiempo real demostró su compromiso con la mejora continua.

Cristian Iván López Meneses

Mi experiencia fue en la verificación y documentación detallada de los datos catalogados. Su enfoque sistemático para realizar pruebas aleatorias y cruzadas garantizó la integridad y confiabilidad de la información recopilada. Además, su habilidad para presentar los hallazgos de manera clara y concisa facilitó la comprensión y uso del catálogo por parte de otros miembros del equipo y usuarios finales. Cristian también jugó un papel vital en la presentación y revisión del catálogo, asegurando que todas las sugerencias y comentarios fueran incorporados adecuadamente.


### Conclusión General
La creación de un catálogo de datos para un Data Lakehouse es una tarea compleja que requiere una planificación meticulosa, la implementación de herramientas automatizadas y un enfoque colaborativo. Este proyecto ha demostrado la importancia de establecer un entorno de trabajo robusto utilizando tecnologías como Docker y WSL2, lo que permite una instalación y configuración eficientes de las herramientas necesarias. La automatización del proceso de catalogación a través de scripts desarrollados específicamente ha permitido una exploración y documentación exhaustiva de los conjuntos de datos, mejorando la organización y accesibilidad de la información.
La verificación y documentación detallada son esenciales para asegurar la precisión y exhaustividad del catálogo, proporcionando una base confiable para futuras investigaciones y análisis. La colaboración entre los miembros del equipo y la incorporación de comentarios de usuarios han sido cruciales para refinar y mejorar la documentación, garantizando que el catálogo final sea útil y preciso.
Además, la facilidad de acceso y uso del catálogo en formatos digitales accesibles (.xlsx o .csv), complementado con presentaciones claras y concisas, facilita su consulta y utilización por parte de los interesados. Las recomendaciones para la actualización continua del catálogo, la capacitación de los usuarios, la evaluación periódica y la consideración de la escalabilidad del sistema son fundamentales para asegurar la sostenibilidad y efectividad a largo plazo del catálogo de datos.
En resumen, este proyecto ha sido un ejemplo exitoso de cómo la combinación de tecnología, automatización y colaboración puede llevar a la creación de un recurso invaluable para científicos e ingenieros de datos, facilitando la gestión y el análisis eficiente de grandes volúmenes de datos y, en última instancia, apoyando la toma de decisiones informadas y basadas en datos.

## Competencias desarrolladas y/o aplicada

Ernesto Yael Ponce Gómez

1.	Configuración de Entornos de Trabajo:

•	Instalación y configuración de Docker y WSL2 para crear un entorno robusto de desarrollo y ejecución.
•	Configuración de bases de datos opcionales utilizando PostgreSQL.

2.	Manejo de Contenedores:

•	Implementación y gestión de contenedores para ejecutar diversas herramientas de catalogación de datos.
•	Uso de Podman para gestionar contenedores, incluyendo la descarga e inicialización de imágenes de contenedores.

3.	Solución de Problemas Técnicos:

•	Identificación y resolución de problemas técnicos durante la implementación de contenedores y configuración de bases de datos.
•	Capacidad para solucionar rápidamente errores comunes al instalar y configurar software en entornos virtualizados.

4.	Automatización de Procesos:

•	Desarrollo de scripts automatizados para la exploración y catalogación de conjuntos de datos.
•	Automatización de la generación de archivos consolidados que documentan los detalles de cada conjunto de datos.

5.	Documentación Técnica:

•	Documentación detallada de la configuración del entorno de trabajo y de los procedimientos de instalación de software.
•	Creación de guías paso a paso para la instalación y configuración de herramientas esenciales.

6.	Habilidades en Desarrollo de Software:

•	Uso de Node.js y Express para crear una API que manipula diferentes tipos de datos.
•	Implementación de rutas en la API para operaciones con CSV, JSON, Parquet, Avro, imágenes, audio, video, PDF, y GeoJSON.

7.	Gestión de Bases de Datos:

•	Configuración de MySQL y PostgreSQL en entornos de contenedores.
•	Migración de bases de datos de MySQL a PostgreSQL utilizando DM Toolkit.

Lauro Manuel Cárdenas Herrera

1.	Exploración de Datos:

•	Uso de Jupyter Lab y bibliotecas como pandas para la exploración inicial de datos.
•	Identificación de características clave de los datos como el esquema, formato, tamaño y descripción del contenido.

2.	Automatización de la Catalogación de Datos:

•	Desarrollo de scripts para automatizar la catalogación de datos, mejorando la eficiencia y precisión del proceso.
•	Generación de archivos consolidados que documentan los detalles de cada conjunto de datos.

3.	Verificación y Validación de Datos:

•	Realización de pruebas aleatorias y cruzadas para verificar la precisión y exhaustividad del catálogo de datos.
•	Documentación detallada de la verificación y validación de los datos catalogados.

4.	Integración de Comentarios de Usuarios:

•	Presentación del catálogo final y recepción de comentarios de los usuarios.
•	Incorporación de sugerencias y ajustes en tiempo real para mejorar la documentación y la utilidad del catálogo.

5.	Mejora Continua:

•	Identificación de áreas de mejora en el proceso de catalogación y documentación.
•	Implementación de mejoras basadas en la retroalimentación recibida de usuarios y miembros del equipo.

6.	Colaboración en Equipo:

•	Trabajar de manera colaborativa con otros miembros del equipo para asegurar la precisión y utilidad del catálogo.
•	Participación en reuniones y presentaciones para discutir avances y recibir retroalimentación.

7.	Presentación de Resultados:

•	Creación de presentaciones claras y concisas que explican los hallazgos del proceso de catalogación.
•	Generación de archivos digitales accesibles (.xlsx o .csv) con la información detallada de cada conjunto de datos.

8.	Ejecución de contenedores

•	Configuración y ejecución de lo contenedores 

Cristian Iván López Meneses

Aprendizaje obtenido

1. Instalación de WSL2 

•	Activar WSL2
Seleccionar “Subsistema de Windows para Linux y máquina virtual “para su instalación.
•	Instalar Ubuntu 

2. Descargar desde Microsoft Store Ubuntu.

Configuración del contenedor de postman API

•	Crear un proyecto en Node.js
Ejecución de diferentes comandos para la creación del Node.js, por ejemplo: mkdir api-server y npm init -y.

•	Instalar Express 
Instalar Express y otros paquetes necesarios, comando utilizado: npm install express body-parser mysql2. 

•	Creación y configuración del archivo “server.js”
Instalar librerías adicionales, como: csv-parser csv-writer parquetjs avsc sharp fluent-ffmpeg pdf-lib html-pdf winston shapefile geojson y parquetjs-lite.

3.Configuración MySQL en XAMPP
•	Iniciar los módulos de apache y MySQL 
•	Creación de una base de datos llamada “testdb”

4.Pruebas con postman

•	Pruebas 
Hacer pruebas con los métodos post y get con la API desarrollada para los archivos: csv, json, parquet, avro, imágenes, audio, video, pdf, geojson y archivos tiff.

5.Instalación de podman

•	Inicialización de podman: 
Abrir podman e inicializar los servicios 
•	Descargar imágenes de contenedores  
Uso de comandos “podman pull” para descargar las imágenes de los conedores necesarios desde DockerHub.
•	Configurar y ejecutar contenedores
Configuración para iniciar el contenedor correspondiente 

6.Migración de MySQL a PostgreSQL usando DM Toolkit

•	Ejecutar DM Toolkit
Seleccionar la base de datos MySQL a migrar y el destino PostgreSQL
Completar los pasos para migrar las tablas deseadas.
•	Exportar base de datos 
En pgAdmin seleccionar la base de datos migrada 
Guardar el respaldo en el formato “custom”
 
7.Administración de contenedores Docker 

•	Descargar imágenes 

Utilización de comando para descargar imágenes de openmetadata desde Docker hub, por ejemplo: Docker pull openmetadata/docs, docker pull openmetadata/ingestión y docker pull openmetadata/server.

•	Ejecutar contenedores 

Configuración y ejecución de lo contenedores 

## Referencias 
1.	Postman documentation overview | Postman Learning Center. (2023, 19 octubre). Postman Learning Center. https://learning.postman.com/docs/introduction/overview/
2.	Rodríguez, D. (2018, 26 octubre). Archivos JSON con Python: lectura y escritura. Analytics Lane. https://www.analyticslane.com/2018/07/16/archivos-json-con-python/#google_vignette 
3.	GeoJSON—Portal for ArcGIS | Documentación de ArcGIS Enterprise. (s. f.). https://enterprise.arcgis.com/es/portal/latest/use/geojson.htm
4.	 Iqbal, K. (2019, 10 septiembre). TIFF - Formato de archivo de imagen. https://docs.fileformat.com/es/image/tiff/
5.	Craigloewen-Msft. (2023, 28 agosto). Instalación de WSL. Microsoft Learn. https://learn.microsoft.com/es-es/windows/wsl/install  
6.	Equipo editorial de IONOS. (2023, 1 marzo). XAMPP: instalación y primeros pasos. IONOS Digital Guide. https://www.ionos.mx/digitalguide/servidores/herramientas/instala-tu-servidor-local-xampp-en-unos-pocos-pasos/
7.	¿Qué es un catálogo de datos? | IBM. (s. f.). https://www.ibm.com/mx-es/topics/data-catalog

8.	Podman Installation | Podman. (s. f.). https://podman.io/docs/installation
9.	Create your first collection | Postman Learning Center. (2024, 24 mayo). Postman Learning Center. https://learning.postman.com/docs/getting-started/first-steps/creating-the-first-collection/
10.	Cómo Instalar PostgreSQL 2024 actualizado en Windows 11 - Blog Grupo Codesi. (s. f.). Grupo Codesi. https://www.grupocodesi.com/blog/instalar-postgresql.html
