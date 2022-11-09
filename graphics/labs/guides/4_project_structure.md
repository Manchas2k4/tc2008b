# Estructuración de Proyectos en Unity

## Objetivo
En este laboratorio más allá de crear funcionalidad particular hablaremos de varios puntos específicos que ayudarán el desarrollo colaborativo de tu proyecto. Tando del lado de Unity como del lado de Github, algunas buenas prácticas en general para el desarrollo de proyectos de Unity, como buenas prácticas en el desarrollo de Software en general.

Toma los conocimientos vistos en este laboratorio para el desarrollo ágil de tu proyecto.

## Instrucciones
Sigue los pasos descritos en la siguiente práctica, si tienes algún problema no olvides que tus profesores están para apoyarte.

## Laboratorio
### Paso 1 Crear un nuevo repositorio

**Nota: Este proyecto no tendrá mucho contenido a nivel funcional, solo manejaremos la estructuración básica del proyecto y algunas recomendaciones generales para Github en Unity.**

Crea un repositorio en Github y clonalo en tu máquina para empezar. Verifica que el .gitignore del proyecto traiga el de Unity.

En micaso estaré usando línea de comando pero puedes utilizar cualquier GUI si te acomodas más, incluso Unity tiene su integración de Github que puedes utilizar.

![graficas](/graphics/assets/img/lab4/1_lab4.png)

![graficas](/graphics/assets/img/lab4/2_lab4.png)

Crea un nuevo proyecto 3D como lo hemos estado haciendo en Laboratorios anteriores dentro la carpeta de tu repositorio.

Lo primero que vamos a hacer es explorar el archivo .gitignore que trae el repositorio.

En las primeras líneas veras que hay varias líneas comentadas. Vamos a quitarles el **/** y dejarlas de la siguiente forma.

```
[Ll]ibrary/
[Tt]emp/
[Oo]bj/
[Bb]uild/
[Bb]uilds/
[Ll]ogs/
[Mm]emoryCaptures/
```
De esta manera evitaremos subir los archivos que pueden causar mayor confusión a un proyecto.

### Paso 2 Estructuración de escena

Una vez modificado el .gitignore vamos a saltar a Unity.

Dentro de Unity vamos a comenzar retomando los objetos vacíos. Un objeto vacío es algo que no genera recursos pero nos puede servir de muchas maneras, tanto para ejecutar scripts globales como el del tiempo del laboratorio anterior. Como para agrupar conjuntos de objetos entre sí, si bien podemos verlos por lo que son como objetos dentro de la escena, también podemos visualizarlos como carpetas que podemos usar a nuestro favor para organizar nuestro proyecto.

Vamos a crear varios objetos vacíos y vamos a estructurar una jerarquía como se muestra a continuación en la imagen.

![graficas](/graphics/assets/img/lab4/3_lab4.png)

Como resumen tenemos:
- **Managers:** Son los que nos ayudan a administrar nuestro juego.
- **Setup:** Es donde colocamos los ajustes generales de la escena como cámaras, luces, sistemas de eventos, etc.
- **Environment:** Donde colocamos los bloques que conforman el nivel como pueden ser los tiles de un mapa, el terreno, o para el caso de tu proyecto los carriles. También podemos agregar elemntos más pequeños como árboles, obstáculos que sean propios del mismo ambiente. Para agrupar mejos estos elementos incluso podemos agregar un nivel extra de **Units** para agrupar estos elementos.
- **Canvases:** Bastante directo, es donde colocamos los canvas del proyecto, normalmente podemos tener entre 1 o 2 por proyecto.
- **Systems:** Son los únicos elementos que tienen implementado el no destruirse al cargar el proyecto o que sean de alguna manera persistentes, en el caso del ejemplo la música sería un caso concreto.

Esto nos ayudará a separar más concretamente los elementos que conforman nuestra escena.

### Paso 3 Estructuración de Assets

Para nuestro proyecto es importante que separemos en carpetas los diferentes assets que vamos a tener disponibles para trabajar.

Las carpetas normales que pudieramos llegar a tener se muestran a continuación.

![graficas](/graphics/assets/img/lab4/4_lab4.png)

Si llegaramos a importar algún paquete de assets por ejemplo de la tienda es probable que se cree su propia carpeta y en este caso no haya problema. Solo cuida la cantidad de adicionales que agregas ya que los assets en videojuegos pueden llegar a crecer, si tu repositorio es gratuito verifica el límite que tienes disponible para que esto no se vuelva un conflicto hacia adelante.

### Paso 3 Arquitectura de Proyecto en Unity

Como mencionamos en el Laboraroio 2, si bien no es absolutamente necesario el agregar arquitectura en un proyecto de Unity, a nivel de Ingeniería de Software se recomienda aplicar esto para tener un mejor control sobre los cambios, pruebas y elementos específicos que involucran el código.

Como ya mencionamos también, la clase **Monobehaviour** es la que nos permite conectar elementos de nuestra escena al código como tal. Si bien existen otros tipos de scripts en Unity, no es alcance del curso verlos. Pero si empezamos a implementar arquitectura como lo hicimos en el laboratorio anterior podemos tener una simple arquitectura MVC, a lo cual solo agregaríamos las carpetas correspondientes y recuerda todo lo que tiene que ver con el Framework de Unity serían las Vistas, de ahí en fuera dependerá de nosotros como estructuremos los Modelo (Entidades y Services de conexión) y Controladores para estar llamando entre unos y otros.

Como quiero hacer un poco más detallada la arquitectura contigo vamos a añadir la meta arquitectura Clean, esto para lograr repartir un grupo de requerimientos en nuestro proyecto. Si aún no conoces esta meta arquitectura, nos permite trabajar en conjunto con otras arquitecturas como MVC, pero a nivel de estructurar requerimientos.

Para hacerlo más visible vamos a hacer las distintas carpetas para el proyecto.

![graficas](/graphics/assets/img/lab4/5_lab4.png)

La **Clean Architecture** contiene las siguientes capas:
- **Data:** En esta capa se toca todo lo relacionado con los datos y entidades, comunmente es lo que guardaríamos en las bases de datos como objetos, pero dado que estamos hablando de juegos, aquí podemos tener elementos propios con sus propiedades colo la clase **Bullet**. Por último se tiene una clase **Repository**, esta nos permite administrar información de diferentes fuentes de datos como es una BD, una BD Local,etc. Hoy en día no solo tenemos juegos que se conectan o no a internet, sino que son híbridos en sus características, entonces para poder manejar esto utilizamos este patrón de diseño.
- **Domain:** Esta capa sería el desglose de cada uno de nuestros requerimientos, en otras fuentes puedes encontrarlo a nivel de Historias de Usuario o Use Cases, pero para poder extenderlo y no limitarlo a desarrollo ágil solo lo llamaremos **Requirements**.
- **Framework:** Será la capa que integre todo lo que tiene que ver con el Framework de Unity, clases propias y aquí es donde inicia la llamada desde las vistas hacia los controladores que mandan llamar requerimientos del proyecto.

Adicional a la **Clean Architecture**, tenemos un folder llamado **Utils**, este normalmente se usa para generalizar funciones muy propias del lenguaje de programación usado que se pueden compartir entre todos los elementos de la arquitectura, un ejemplo muy conreto es un archivo de Constantes para todo el proyecto.

La parte más importante de todo lo que tiene que ver en cuestión de organización, es que si bien hay algunar sugerencias, la mejor forma es como lo decidan como equipo. Incluso los nombres no están escritos en piedra, apliquen los que se les hagan más representativos.

### Paso 3 Conflictos en las escenas

Si hasta este punto del curso ya has intentado hacer algun guardado de forma colaborativa con un repositorio, notarás que es muy difícil trabajar entre todos en la escena, puesto que al ser un solo elemento cualquier cambio puede generar conflictos.

Si bien es cierto que deben ponerse de acuerdo en quien trabajará la escena, el secreto a evitar cambios y conflictos al momento de hacer commits está en los prefabs.

Y vamos a analizar el concepto para que haga snetido, los prefabs son construcciones personalizadas de objetos que ya tienen propiedades y componentes específicos e incluso ya tienen sus pocisiones.

Con esta técnica inicialmente trabajaremos con la escena configurada de manera general por todos los miembros del equipo, y después asignaremos a cada miembro una tarea específica de diseño de la escena.

Para tu proyecto podemos tener el siguiente ejemplo:

1. Todos deciden y colocan el terreno en la escena.
2. Se asigna a un miembro del equipo a trabajar en los autobuses.
3. Otro miembro se encarga de los obstáculos
4. Otro miembro se encarga de los peatones.
5. Cada miembro puede añadir tantos elementos como necesite a la escena siempre y cuando al final deberá crear un prefab y agrupar todos los elementos de trabajo, y eliminarlos de la escena.
6. Cuando se termina la tarea se hacen los commits correspondientes y al final una persona se encarga de integrar nuevamente los prefabs en la escena ya en su lugar final, al estar habilitado el prefab ya se contará con toda la configuración y programación necesaria para todos los elementos y podrán avanzar a la siguiente tarea.

Usa todos los elementos de agrupación para el caso de objetos y Progrmaación Orientada a Objetos para tus scripts en conjunto con tu arquitectura para hacer más fácil la colaboración.

Es cierto que habrá redundancia en ciertos archivos u objetos, pero verás que a la larga será mejor el desarrollo y tendrás mucho mayor calidad en el proyecto.

Haz commit de tus cambios e intenta hacer una prueba con tu equipo para que les haga sentido todos estos conceptos vistos.

## Comentarios Adicionales

1. No olvides hacer un desarrollo en GitHub orientado a Gitflow para desarrollar en base a funcionalidades, cada branch debe ser un feature, y no olvides tener reuniones de integración para evitar conflictos.
2. Los conflictos del repositorio se dan por cambios en muchos días de trabajo, busca iteraciones cortas e incluso si puedes implementa una metodología de Administración de Proyectos para mayor control.
3. Crea plantillas para tus Pull Requests, GitHub, te permite crear plantillas donde especifiquen como equipo cual debe ser el proceso que necesitan seguir desde análisis, diseño, implementación y pruebas, para que una funcionalidad sea aprobada. El tiempo que tienen es poco pero si se dan un tiempo para definir esto van a hacer más eficiente su desarrollo.
4. No olvides lo que has aprendido hasta este punto en la carrera.