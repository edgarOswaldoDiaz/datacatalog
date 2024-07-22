## Índice
- INTEGRANTES
- ASESOR
- LABORATORIO DE CIENCIA DE DATOS
- Requerimientos de instalación
- Instalación de Postman
- Instalación de WSL2
- Configuración de contenedores API en Postman
- Código
- Descripción del código
- Continuación de configuración de contenedores API
- Pruebas de contenedor
- Solicitudes en Postman
  1. Leer CSV
  2. Escribir CSV
  3. Leer JSON
  4. Escribir JSON
  5. Leer Parquet
  6. Escribir Avro
  7. Leer Avro
  8. Procesar Imagen
  9. Convertir Audio
  10. Convertir Video
  11. Crear PDF
  12. Convertir a GeoJSON
  13. Convertir TIFF
- Referencias APA
- Conclusión

## Requerimientos de instalación

### Instalación de Postman
1. En el navegador buscamos Postman y seleccionamos la segunda opción para descargar que será Download Postman.
2. Ingresamos a la página de Postman y descargamos para Windows 64-bit o 32-bit, según nuestra arquitectura de computadora.
3. Antes de continuar, pedirá que se ingrese un correo electrónico. En este caso, creamos una cuenta nueva.
4. Es necesario llenar el formulario con los datos solicitados.
5. Una vez llenado los campos y creada la cuenta, abrimos Postman.
6. Es importante asignar un nombre de usuario y un rol.

### Instalación de WSL2
1. Buscamos "Activar o desactivar características de Windows" y damos enter.
2. Nos abrirá una pestaña con varias opciones. Seleccionamos "Subsistema de Windows para Linux" y "Virtual Machine Platform" para poder activar Ubuntu en nuestra computadora sin necesidad de descargar una máquina virtual.
3. Buscamos en el buscador de nuestra computadora la tienda oficial de Microsoft Store y damos enter.
4. Descargamos e instalamos Ubuntu para hacer las pruebas necesarias con todos los contenedores que requerimos.
5. Estos serán todos los pasos para instalar WSL2 y poder hacer todas nuestras pruebas.

### Contendores postman api configuración

1. Creamos un proyecto en Node.js
•	Abrimos la una terminal con la ruta donde desemos crear nuestro en la ubicación que gustemos y corremos los siguientes comandos:

mkdir api-server
cd api-server

•	Ahora inicilizaremos nuestro proyecto correindo el siguiente comando en la ruta de dicho proyecto o terminal:

npm init -y
 
2. Instalar Express
•	Instalaremos Express junto con sus paquetes necesarios con el siguiente comando:

npm install express body-parser mysql2

 
