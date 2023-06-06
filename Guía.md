# Guía para ingestar datos en amundsen

En la terminal de Linux ejecutar los siguientes comandos, todo en modo superusuario
- Clonar el proyecto de amundsen
#git clone --recursive https://github.com/amundsen-io/amundsen.git

- Entrar al proyecto, entra a la carpeta del proyecto con
#cd amundsen/ 

- Edita el archivo docker-amundsen.yml con
#vi docker-amundsen.yml 

- Posteriormente concede permisos a los volumenes de Neo4j, agregando :z en las 3 primeras lineas de los volumenes de neo4j, como se muestra a continuación, cuida que estas 4 líneas de código queden al mismo nivel
![imagen](https://github.com/edgarOswaldoDiaz/datacatalog/assets/91812737/f87d24ee-9329-46e4-b2a6-8e0b4659e9e7)
- Guarda el archivo con estos permisos ejecuta el siguiente comando para levantar todos los servicios de amundsen
#podman-compose -f docker-amundsen-yml up

- Abre una nueva terminal, descarga los siguientes archivos y pegalos en la siguiente ruta - amundsen/databuilder/example/sample_data
[data_col.csv](https://github.com/edgarOswaldoDiaz/datacatalog/files/11670915/data_col.csv)
[data_owner.csv](https://github.com/edgarOswaldoDiaz/datacatalog/files/11670916/data_owner.csv)
[data_table.csv](https://github.com/edgarOswaldoDiaz/datacatalog/files/11670917/data_table.csv)

- Abre una nueva terminal, descarga el siguiente script y pegalo en la siguiente ruta - amundsen/databuilder/example/scripts, este script es de Python por lo que deberás renombrarlo con la extension .py
[data_json.txt](https://github.com/edgarOswaldoDiaz/datacatalog/files/11670728/data_json.txt)

- Abre una nueva terminal y dirigete a la carpeta de databuilder con
#cd databuilder/
- Ejecuta los siguientes comandos 
#python3 -m venv venv
#source venv/bin/activate
#pip3 install --upgrade pip
#pip3 install -r requirements.txt
#python3 setup.py install
- Ejecuta el script
#python3 example/scripts/data_json.py
- Abre tu navegador en http://localhost:5000 y comprueba que tienes 189 datasets realizando una busqueda.

