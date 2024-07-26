Índice
INTEGRANTES: 1
ASESOR: 1
LABORATORIO DE CIENCIA DE DATOS 1
Introducción 2
Objetivos 3
Mecanismos de Seguridad en OpenMetadata 5
Vulnerabilidades en OpenMetadata 7
Recomendaciones para Mitigar Riesgos 8
Ventajas 9
Desventajas 9
Referencias 10

## Introducción

OpenMetadata es una plataforma de gestión de metadatos de código abierto diseñada para facilitar la gobernanza, el descubrimiento y la colaboración de datos en diversas fuentes de datos. Con el creciente volumen de datos y la complejidad de los entornos de datos modernos, la necesidad de una herramienta que centralice y gestione los metadatos de manera eficiente se ha vuelto crucial. OpenMetadata se presenta como una solución robusta, proporcionando un repositorio centralizado que permite a los usuarios entender y gestionar sus activos de datos a través de funcionalidades avanzadas como el linaje de datos, la catalogación y la gobernanza de datos.
La plataforma permite a las organizaciones obtener una visión completa de sus datos, mejorando la toma de decisiones, la eficiencia operativa y la conformidad regulatoria. OpenMetadata soporta una amplia variedad de fuentes de datos, desde bases de datos tradicionales hasta plataformas de big data, servicios de almacenamiento en la nube y más, lo que la hace extremadamente versátil y adaptada a diferentes necesidades empresariales.
A pesar de su utilidad y sofisticación, OpenMetadata, como cualquier otra plataforma de software, no está exenta de vulnerabilidades de seguridad. Las plataformas que gestionan información crítica, como los metadatos, son objetivos atractivos para los atacantes, y las brechas de seguridad pueden tener consecuencias graves. Las vulnerabilidades pueden comprometer la integridad y confidencialidad de los datos, interrumpir los servicios y, en casos extremos, permitir el control total del sistema por parte de actores maliciosos.
Este documento tiene como objetivo detallar los mecanismos de seguridad inherentes en OpenMetadata, proporcionar un análisis de las vulnerabilidades descubiertas y ofrecer recomendaciones para mitigar los posibles riesgos. La seguridad de la plataforma es crítica para proteger la integridad y confidencialidad de los datos, así como para evitar interrupciones de servicio y el control no autorizado del sistema.

## Objetivos

El objetivo principal de este documento es analizar y fortalecer la seguridad de OpenMetadata. Para lograrlo, se han establecido los siguientes objetivos específicos:

1. Describir los Mecanismos de Seguridad Actuales:
   Proporcionar una descripción detallada de los mecanismos de autenticación, autorización y cifrado implementados en OpenMetadata para proteger los metadatos y el acceso a la plataforma.

2. Identificar Vulnerabilidades:
   Analizar las vulnerabilidades de seguridad que se han descubierto en versiones anteriores de OpenMetadata, especificando su naturaleza y el impacto potencial en la plataforma y sus usuarios.

3. Recomendar Medidas de Mitigación:
   Ofrecer recomendaciones claras y prácticas para mitigar los riesgos asociados a las vulnerabilidades identificadas, incluyendo la actualización de la plataforma, la implementación de autenticación multifactor y la segmentación de la red.

4. Proporcionar Guías de Mejores Prácticas:
   Sugerir mejores prácticas y configuraciones adicionales de seguridad que las organizaciones pueden implementar para asegurar sus entornos de OpenMetadata de manera efectiva.

5. Promover la Preparación y Resiliencia:
   Destacar la importancia de tener planes de respuesta a incidentes y estrategias de recuperación de datos, asegurando que las organizaciones estén preparadas para manejar y recuperarse de posibles violaciones de seguridad.

Con estos objetivos, este documento busca proporcionar a los administradores de OpenMetadata y a los profesionales de TI una guía comprensiva y accionable para mejorar la seguridad de sus implementaciones de OpenMetadata.

## Mecanismos de Seguridad en OpenMetadata

1.	Autenticación y Autorización 
OpenMetadata emplea mecanismos robustos de autenticación y autorización para garantizar que solo los usuarios autorizados puedan acceder o modificar los metadatos. Los métodos principales incluyen:

Tokens Web JSON (JWT): 
•	OpenMetadata usa JWT para la autenticación de API. Los JWT son un método seguro para transmitir información entre partes como un objeto JSON. Esta autenticación basada en tokens asegura que solo los usuarios con tokens válidos puedan acceder al sistema.

OAuth 2.0: 
•	La integración con OAuth 2.0 permite a los usuarios autenticarse a través de proveedores de identidad de terceros, mejorando la seguridad al aprovechar marcos de autenticación existentes.

Control de Acceso Basado en Roles (RBAC): 
•	El RBAC se implementa para proporcionar un control de acceso granular. Se asignan roles a los usuarios, cada uno con permisos específicos, asegurando que el acceso a metadatos sensibles esté restringido según los roles y responsabilidades de los usuarios.

2.	Cifrado 
Para proteger los datos en tránsito y en reposo, OpenMetadata utiliza cifrado:

TLS/SSL: 
•	La seguridad de la capa de transporte (TLS) y la capa de sockets seguros (SSL) se utilizan para cifrar los datos transmitidos a través de la red, evitando el acceso no autorizado y garantizando la integridad de los datos.

Cifrado AES: 
•	El estándar de cifrado avanzado (AES) se utiliza para cifrar datos sensibles almacenados en el sistema, como credenciales de usuario y configuraciones.

3.	Registro de Auditoría 
OpenMetadata mantiene registros de auditoría detallados de todas las actividades de los usuarios y eventos del sistema. Estos registros son cruciales para:

Monitoreo y Cumplimiento: 
•	Los registros proporcionan un registro de acceso y modificaciones a los metadatos, ayudando en el cumplimiento de los requisitos regulatorios.

Respuesta a Incidentes: 
•	En caso de una violación de seguridad, los 
•	registros de auditoría son invaluables para el análisis forense y la comprensión del alcance del compromiso.

## Vulnerabilidades en OpenMetadata

Evaluaciones de seguridad recientes han identificado varias vulnerabilidades críticas en versiones de OpenMetadata anteriores a la 1.3.1. Estas vulnerabilidades han sido explotadas activamente, particularmente en entornos de Kubernetes:

1.	Evasión de Autenticación (CVE-2024-28255) 
•	Esta vulnerabilidad permite a los atacantes eludir los mecanismos de autenticación, obteniendo acceso no autorizado al sistema. Al explotar esta falla, los atacantes pueden ejecutar operaciones privilegiadas sin credenciales válidas, comprometiendo la integridad y confidencialidad de los metadatos.

2.	Ejecución Remota de Código (RCE) 
•	Varias vulnerabilidades (CVE-2024-28847, CVE-2024-28253, CVE-2024-28848, CVE-2024-28254) permiten a los atacantes ejecutar código arbitrario en contenedores que ejecutan versiones vulnerables de OpenMetadata. Esto puede llevar a un control total sobre el sistema comprometido, permitiendo a los atacantes desplegar malware, robar información sensible o interrumpir servicios.

3.	Ataques de Criptominería 
Al explotar las vulnerabilidades mencionadas anteriormente, los atacantes han desplegado malware de criptominería en entornos comprometidos. Estos ataques típicamente implican:

Acceso Inicial: 
•	Los atacantes identifican y apuntan a cargas de trabajo de Kubernetes de OpenMetadata expuestas a Internet. Al identificar sistemas que ejecutan versiones desactualizadas y vulnerables de la aplicación, los atacantes pueden obtener acceso no autorizado.

Reconocimiento: 
•	Después de obtener acceso, los atacantes validan su control realizando un reconocimiento. Esto implica consultar configuraciones de red, extraer variables de entorno (que pueden contener credenciales) y evaluar el sistema para una mayor explotación.

Despliegue de Payload: 
•	Una vez confirmado el acceso, los atacantes descargan y ejecutan malware de criptominería desde un servidor remoto. Este malware utiliza los recursos del sistema comprometido para la minería de criptomonedas, a menudo llevando a una degradación significativa del rendimiento.

## Recomendaciones para Mitigar Riesgos
Para protegerse contra estas vulnerabilidades y asegurar las implementaciones de OpenMetadata, se recomiendan las siguientes medidas:
1.	Actualizar a la Última Versión Asegúrese de que las instalaciones de OpenMetadata estén actualizadas a la versión 1.3.1 o posterior. Aplicar regularmente parches de seguridad y actualizaciones es crucial para protegerse contra vulnerabilidades recién descubiertas.
2.	Implementar una Autenticación Fuerte
•	Evitar Credenciales Predeterminadas: Asegúrese de que las credenciales predeterminadas se cambien por contraseñas fuertes y únicas.
•	Usar Autenticación Multifactor (MFA): Implemente MFA para proporcionar una capa adicional de seguridad, requiriendo que los usuarios proporcionen dos o más factores de verificación para obtener acceso.
3.	Segmentación de Red y Controles de Acceso
•	Limitar la Exposición: Restrinja la exposición a Internet de las cargas de trabajo de Kubernetes que ejecutan OpenMetadata. Use firewalls y segmentación de red para limitar el acceso solo a fuentes confiables.
4.	Monitoreo y Auditoría
•	Auditorías Regulares: Realice auditorías de seguridad y evaluaciones de vulnerabilidad regularmente para identificar y remediar posibles debilidades.
•	Monitoreo Continuo: Implemente soluciones de monitoreo continuo para detectar y responder a actividades sospechosas. Utilice herramientas como Microsoft Defender for Cloud para identificar y mitigar actividades maliciosas en tiempo real.
5.	Respuesta a Incidentes y Recuperación
•	Preparación: Desarrolle y mantenga un plan de respuesta a incidentes para abordar y recuperarse rápidamente de violaciones de seguridad.
•	Copias de Seguridad: Realice copias de seguridad regularmente de datos y configuraciones críticas. Asegúrese de que las copias de seguridad estén almacenadas de manera segura y puedan ser restauradas en caso de un ataque de ransomware o pérdida de datos.


<table>
  <thead>
    <tr>
      <th>Ventajas</th>
      <th>Desventajas</th>
    </tr>
  </thead>
</table>

## Conclusión general

El proyecto de construcción de un data catalog para un data lakehouse utilizando OpenMetadata se centra en la gestión eficiente y segura de metadatos en un entorno de datos moderno. OpenMetadata se presenta como una solución robusta que centraliza y facilita la gobernanza, el descubrimiento y la colaboración de datos provenientes de diversas fuentes. Su implementación permite a las organizaciones tener una visión integral de sus activos de datos, mejorando la toma de decisiones y la eficiencia operativa, así como garantizando el cumplimiento regulatorio.

A pesar de sus ventajas, OpenMetadata no está exento de vulnerabilidades. Las evaluaciones de seguridad han identificado varias fallas críticas en versiones anteriores a la 1.3.1, que pueden comprometer la integridad y confidencialidad de los datos. Entre estas vulnerabilidades se incluyen la evasión de autenticación y la ejecución remota de código, las cuales pueden ser explotadas por atacantes para obtener acceso no autorizado o controlar el sistema.

Para mitigar estos riesgos, es esencial actualizar a la última versión de OpenMetadata y aplicar regularmente parches de seguridad. Además, se recomienda implementar autenticación multifactor, segmentación de red y controles de acceso basados en el principio de mínimo privilegio. También es crucial mantener un monitoreo continuo y desarrollar planes de respuesta a incidentes, junto con la realización de copias de seguridad periódicas para asegurar la recuperación de datos en caso de ataques.

En resumen, la construcción de un data catalog con OpenMetadata ofrece una solución eficiente para la gestión de metadatos, pero requiere una atención constante a la seguridad y la implementación de mejores prácticas para mitigar posibles vulnerabilidades y asegurar la integridad de los datos.

## Referencias

OpenMetadata Docs. (s. f.). https://docs.open-metadata.org/v1.4.x 
 CVE Details: "Vulnerability Details for CVE-2024-28255." CVE Details, 2024, https://www.cvedetails.com/cve/CVE-2024-28255/.

OWASP: "OWASP Top Ten Security Risks." OWASP Foundation, https://owasp.org/www-project-top-ten/.

NIST: "National Institute of Standards and Technology. NIST Cybersecurity Framework." NIST, https://www.nist.gov/cyberframework.

Kubernetes: "Kubernetes Security Best Practices." Kubernetes Documentation, https://kubernetes.io/docs/concepts/security/.

Microsoft Defender for Cloud: "Microsoft Defender for Cloud Documentation." Microsoft, https://learn.microsoft.com/en-us/azure/defender-for-cloud/.

