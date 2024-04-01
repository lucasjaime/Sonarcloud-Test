Fase 1

Levantar un EC2 en AWS (Capa FREE) con SonarQube

Abrir un repositorio con un código vulnerable (ejemplo: https://github.com/snoopysecurity/Vulnerable-Code-Snippets o https://github.com/DataDog/vulnerable-java-application )

Armar una github action que ante una acción (PR) analice y devuelva la QG obtenida.

Fase 2

Commitear alguna “fake key” que pueda matchear con un regex de un verdadero secret de AWS key o GPAT.

Realizar un script (no importa el lenguaje) que pueda mediante regex encontrar ese secreto en archivos de código. Esto debe correr de manera local sobre el repositorio descargado, no hace falta mayor automatización.

Entregables:

Acceso al repositorio para revisar la github action.

Posibilidad de ver el flujo en funcionamiento.

Script para la obtención del secreto seleccionado.


Fasae 1: Para la fase se abrió el segundo repositorio vulnerable mencionado como ejemplo una vez sincronizado con sonarcloud brindando correctamente lo secrets necesarios. Luego se creo una github action denominada "Sonarcloud Scan" la cual, al hacer un PR intentando subir código en una nueva Branch, analizará el código fuente y devolverá una QG.
Para el Pull request test se resolvieron los issues solicitando el cambio de declaración de variables en javascript.
![WhatsApp Image 2024-04-01 at 16 49 00_ffea09a6](https://github.com/lucasjaime/Sonarcloud-Test/assets/94329292/1412dfde-f723-4a72-ba6b-34875d50e3bd)
![WhatsApp Image 2024-04-01 at 16 49 57_e0fc6c88](https://github.com/lucasjaime/Sonarcloud-Test/assets/94329292/9d49fc90-f533-4e77-8522-22ef97e710ae)
![image](https://github.com/lucasjaime/Sonarcloud-Test/assets/94329292/66a66906-16ef-446c-a357-0abf0c0ce6ce)
![WhatsApp Image 2024-04-01 at 16 11 10_0302c84a](https://github.com/lucasjaime/Sonarcloud-Test/assets/94329292/0b486dd3-67ac-4d5c-9cf9-a19ae9144e99)
![image](https://github.com/lucasjaime/Sonarcloud-Test/assets/94329292/542bf418-337e-4e15-9727-33c7132e5499)

Fase 2: Para esta fase, fue declarada la variable api_key en "./vulnerable-java-application/src/main/resources/static/js" con un secret inventando en base a la información proporcionada por AWS. Para encontrar este secret mediante una regex se creo el script "regex.py" encontrado en la carpeta principal "./vulnerable-java-application". Para que este sricpt funcione correctamente, se deberá modificar la variable "ruta_repositorio" por el path donde se encuentre almacenado de forma local la modificación, es decir: "./vulnerable-java-application/src/main/resources/static/js". Un ejemplo de esto podría ser el que se encuentra por default en el script, recordar que en python el path debe estar separado por "/" o en su defecto "\\".
![WhatsApp Image 2024-04-01 at 17 17 27_ea98b8e0](https://github.com/lucasjaime/Sonarcloud-Test/assets/94329292/0192f91d-6a2d-4d57-b803-a1cb6df4ff2b)
![WhatsApp Image 2024-04-01 at 18 31 40_ab30a4ed](https://github.com/lucasjaime/Sonarcloud-Test/assets/94329292/6396ef3d-8993-45c1-824b-446ff02eccef)
![WhatsApp Image 2024-04-01 at 17 24 02_19718113](https://github.com/lucasjaime/Sonarcloud-Test/assets/94329292/1c0dd154-980d-4639-b4c7-dac633a27a7d)

