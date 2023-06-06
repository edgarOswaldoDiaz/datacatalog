# Guía para ingestar datos en amundsen

En la terminal de Linux ejecutar los siguientes comandos, todo en modo superusuario
- Clonar el proyecto de amundsen
#git clone --recursive https://github.com/amundsen-io/amundsen.git
- Entrar al proyecto, entra a la carpeta del proyecto con
#cd amundsen/ 
- Edita el archivo docker-amundsen.yml con
#vi docker-amundsen.yml 
- Posteriormente concede permisos a los volumenes de Neo4j, agregando :z en las lineas de los volumenes de neo4j, como se muestra a continuación, cuida que estas 4 líneas de código queden al mismo nivel
  volumes:
    - ./example/docker/neo4j/conf:/var/lib/neo4j/conf:z
    - ./example/docker/neo4j/plugins:/var/lib/neo4j/plugins:z
    - ./example/backup:/backup:z
    - neo4j_data:/data


## Recursos necesarios principales.
Cuando se trabaja contenerización se recomienda utilizar un sistema operativo Linux, en este apartado y en la practica del proyecto se utiliza un sistema 
RedHat con la version 8.7, este sistema es recomendable de usar ya que tiene instalada por defecto la herramienta Podman (el administrador de pods) que es una herramienta 
open source para desarrollar, gestionar y ejecutar los contenedores en los sistemas Linux.

Si se está haciendo uso de un sistema operativo Windows se puede optar por la opción de instalar RedHat en una máquina virtual, entonces se necesitan realizar las siguientes 
acciones:
- Instalar VMware.
- Crear una máquina virtual con una imagen de RedHat.
- Contenerización con Podman

### MVware
Para instalar MVware es posible dirigirse al sitio oficial, descargar el instalador, e instalar el programa, la instalación es sencilla. 

[Descargar MVware Workstation](https://www.vmware.com/mx/products/workstation-pro/workstation-pro-evaluation.html "Descargar MVware Workstation")
