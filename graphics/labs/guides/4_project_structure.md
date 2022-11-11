# Estructuración de Proyectos en Unity

## Objetivo
En este laboratorio más allá de crear funcionalidad particular hablaremos de varios puntos específicos que ayudarán el desarrollo colaborativo de tu proyecto. Tando del lado de Unity como del lado de Github, algunas buenas prácticas en general para el desarrollo de proyectos de Unity, como buenas prácticas en el desarrollo de Software en general.

Toma los conocimientos vistos en este laboratorio para el desarrollo ágil de tu proyecto.

## Instrucciones
Sigue los pasos descritos en la siguiente práctica, si tienes algún problema no olvides que tus profesores están para apoyarte.

## Laboratorio
### Paso 1 Crear un nuevo repositorio

**Nota: Este proyecto no tendrá mucho contenido a nivel funcional, solo manejaremos la estructuración básica del proyecto y algunas recomendaciones generales para Github en Unity.**

Crea un repositorio en Github y clonalo en tu máquina para empezar. Verifica que el .gitignore del proyecto incluya el de Unity.

En mi caso estaré usando línea de comando pero puedes utilizar cualquier GUI si te acomodas más, incluso Unity tiene su integración de Github que puedes utilizar.

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

Crea un nuevo proyecto en 3D y a diferencia de las ocasiones anteriores usa la carpeta del repositorio que acabamos de clonar.

**Nota: Puedes comenzar creando el proyecto primero y desde ahí crear el repositorio para luego vincularlo a GitHub es lo mismo, solo que en este caso tendrás que agregar el .gitignore de manera manual.**

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

![graficas](/graphics/assets/img/lab4/6_lab4.png)

Ahora vamos a ver como se afecta el proyecto haciendo cambios en general sin planificar el resultado.

Dentro de unity vamos a crear un cubo dentro de **Environment>Units** y vamos a moverlo a las posiciones.

x = 10
y = 10
z = 10

![graficas](/graphics/assets/img/lab4/7_lab4.png)

Guarda estos cambios y haz push al repositorio nuevamente.

Si nos vamos a revisar el commit dentro de GitHub observaremos lo siguiente.

![graficas](/graphics/assets/img/lab4/8_lab4.png)

El cambio solo se hace en el archivo de la escena, y justamente por esto es donde si tratamos todos de hacer cambios en la misma comienzan los dolores de cabeza.

Entonces toma en cuenta que cualquier cambio dentro de la escena, no solo en objetos, sino también luces, cámara u otros afectarán este archivo.

Entonces para poder trabajar de manera sencilla vamos a poner en práctica el uso de los prefabs.

Recuerda que la regla aquí es que cada quien trabaje una parte de la escena.

Vamos a duplicar nuestro cubo actual
y vamos a crear un nuevo **EmptyObject** y a este lo llamaramos North Area. A North Area vamos a añadirle nuestros 2 cubos.

Después vamos a resetear las posiciones de los 2 cubos, y solo vamos a desfasar en x el cubo 2 a x = 5.

![graficas](/graphics/assets/img/lab4/9_lab4.png)

Ahora vamos a arrastrar **North Area** a la carpeta de Prefabs de nuestro proyecto.

![graficas](/graphics/assets/img/lab4/10_lab4.png)

Por último vamos a duplicar **North Area** y después vamos a renombrarlo a **South Area**. Y vamos a colocar los cubos de **South Area** en:

Cubo 1:
z = -5

Cubo 2:
x = -5
z = 5

Por último añadimos **South Area** a nuestra carpeta de prefabs. El resultado debería ser algo como lo siguiente.

![graficas](/graphics/assets/img/lab4/11_lab4.png)

Ahora guardamos la escena y vamos a hacer commit y push de la misma.

Si me voy al commit a ver los cambios vamos a ver algo interesante.

![graficas](/graphics/assets/img/lab4/12_lab4.png)

Dentro del código de la escena notaremos que hay una reducción significativa entre los elementos que conforman la escena, esto es por que la inclusión de los prefabs crea internamente ids para cada uno, por lo que se vuelven elementos independientes, pese a que estoy trabajando en la misma parte.

Ahora si me muevo al archivo del prefab, cualquiera de los 2 puedo observar lo siguiente.

![graficas](/graphics/assets/img/lab4/13_lab4.png)

Aquí es donde están todos los cambios visualizados que aparecían en mi escena la primera vez. Con esto aligeramos la carga de trabajo y distribuimos según los elementos que vayamos construyendo.

**Nota: Aplicar esta técnica implica un proceso de análisis y diseño de software. No será suficiente si solo se dividen el trabajo, necesitan planear bien como van a construir la escena y sus objetos, por que recuerda que pueden incluir más componentes, entre ellos Scripts.**

Vamos a editar el North Area, para que quede claro que como ya no tenemos nuevos cambios en la escena, todo se almacenará en el prefab que estamos seleccionando.

Vamos a seleccionar de la carpeta de **prefabs** el  **North Area** y vamos a ver en el **Inspector** la opción que dice **Open**, vamos a darle clic.

![graficas](/graphics/assets/img/lab4/14_lab4.png)

Ahora observa que estamos en un modo especial donde estamos modificando el prefab de manera interna, incluso si lo ves el color de la escena cambia, así como nuestra jerarquía. Este modo nos permite trabajar solo con el **prefab** y hacer todo lo que necesitemos sin afectar la escena.

![graficas](/graphics/assets/img/lab4/15_lab4.png)

En versiones anteriores de Unity, se podían hacer los cambios directos desde la escena y en vez de tener este modo, solo existía un botón llamado **Apply** que actualizaba todos los cambios internos del prefab. Se modificó ya que en ocasiones se seguía modificando la escena y empeza el conflicto en el trabajo colaborativo. Si bien esta opción todavía existe, te recomiendo que hagas los cambios dentro del modo prefab, así te aseguras de no tocar la escena.

Vamos a duplicar los cubos que contie a 4 y vamos a distribuirlos un poco de manera arbitraria.

![graficas](/graphics/assets/img/lab4/16_lab4.png)

Ahora regresaremos a nuestra escena usando el botón de back de la jerarquía.

![graficas](/graphics/assets/img/lab4/17_lab4.png)

Y una vez afuera veremos como nuestro prefab ya está actualizado.

![graficas](/graphics/assets/img/lab4/18_lab4.png)

Guardaremos todo, y ahora haremos push al repositorio.

Si nos vamos a revisar el commit, observemos que ya no aparecen cambios dentro de la escena, de hecho solo se modificó el prefab de **North Area** pese a que agregamos elementos y modificamos pocisiones.


![graficas](/graphics/assets/img/lab4/19_lab4.png)

Con esto espero que te quede más claro como poder trabajar colaborativamente usando Unity, de aquí solo es ponerse creativo y aplicar los procesos de Desarrollo de Software para hacer proyectos grandes, escalables y de alta calidad.

### Paso 4 Changelog

Ya que tenemos el entendimiento de como funciona un proyecto colaborativo en Unity, vamos a extender un poco más este conocimiento y aplicar algunas técnicas de la industria para que esto funcione a nivel de Desarrollo de Software.

En primer lugar vamos a hablar del acrhivo Changelog.md. Si has visto en algunos repositorios, algunos de los archivos clave son el README, en donde vienen las instrucciones o la descripción del repositiorio, y en ocasiones se agega un archivo changelog.

La idea detrás del changelog es que el equipo tenga muy visible cuales son los cambios dentro de las versiones que va generando.

Aunque aún estes en la escuela, te recomiendo ir añadiendo esta buena práctica a tus desarrollos puesto que es más fácil estar revisando este archivo a estar visitando commits anteriores y recordar que es lo que sucede en el proyecto.

Lo tedioso aquí es que debes recordar actualizar el archivo en cada ocasión que vayas modificando algo de forma sustancial.

Una plantilla que puedes tener para armar tu changelog es la siguiente.

[Plantilla Changelog](https://keepachangelog.com/en/1.0.0/)

Aquí podrás encontras más información de como construir el archivo.

En nuestro caso vamos a crear el archivo Changelog.md dentro de nuestro proyecto dentro de la raíz del mismo a la para del readme que trae el repositorio por default.

Dentro de la plantilla notarás que viene este link.

[Semantic Versioning](https://semver.org/spec/v2.0.0.html)

Aquí podrás encontrar información de como enumerar correctamente tus versiones y lo que significa cada número.

Como de momento hemos hecho todos nuestros cambios directamente a main (master) **mala práctica** vamos a cerrar la versión como la 0.0.0.

Algo que he notado al trabajar con el changelog es que te pide colocar a un lado de la versión la fecha de lanzamiento.

Si bien esto sirve para recordar cuando sucede, si las iteraciones para cada elementos son tardadas podemos olvidar cuando se hizo un cambio exactamente.

Es por esto que yo te recomiendo añadir fechas a cada elemento del changelog para llevar un mejor control de cuando se termino alguna funcionalidad, fix o mejora.

Por esto nuestro archivo inicial quedará como lo siguiente.


![graficas](/graphics/assets/img/lab4/20_lab4.png)

A nivel del archivo estos son los elementos.

```
## [0.0.0] - 10/11/2022

### Added 

- Commit inicial del proyecto (10/11/2022).
- Primer commit del proyecto (10/11/2022).
- Actualización inicial de la escena (10/11/2022).
- Creación de prefabs (10/11/2022).
- Update North Prefab (10/11/2022).
```

Como no seguí inicialmente un flujo para ordenar mi código observa que tengo que colocar cada commit para visualizar que sucedió en el repositorio.

Esto no es lo ideal puesto que una función puede tener muchos commits involucrados, por lo tanto voy a mejora mi desarrollo de Git.

Por ahora vamos a añadir una nueva línea que incluya este cambio donde agregamos el changelog.

Desde aquí ya depende de la convención que siga el equipo para poner los últimos cambios hasta arriba o en orden descendente.

Salvamos nuestro archivo y hacemos push al repositorio.

![graficas](/graphics/assets/img/lab4/21_lab4.png)

### Paso 5 GitFlow

Ahora que tenemos bien preparado nuestro repositorio, vamos a hablar del uso del GitFlow, una forma de estructurar el trabajo colaborativo para hacer Desarrollo de Software con Git.

Si bien existen otros métodos, en los últimos años este flujo se ha vuelto uno de los más populares ya que es el que siguen la mayoría de los desarrolladores open source para poder trabajar en proyectos colaborativos de tecnologías emergentes.

Existen varias formas de armar un gitflow, la que te mostraré van en conjunto con la implementación de metodologías agiles para que en una iteración se cumplan un conjunto de funcionalidades.

Sea que estes trabajando tu solo en el repositorio o con equipo grande, mantener esta estructura te dará un conocimiento de como trabaja la industria, por lo que tener estos conocimientos es fundamental si es que aún no trabajas con ello.

Este gitflow, tiene como objetivo que al inicio de cada Sprint o iteración no exista más que la branch de master o main.

Por supuesto puede haber excepciones, puesto que pueden existir funcionalidades o actualizaciones completas que pueden tardard esde días, hasta meses o años. Pero el chiste a todo esto es implementar de a poco para ir extendiendo mejor el uso a poder trabajar con más tiempo.

Este gitflow incluye en una iteración normal lo siguiente.

1. El branch de **master o main** que no debe ser tocado bajo ninguna circunstancia. Muchas empresas bloquean incluso que no se pueda hacer commit a master y que la única forma de hacerlo sea a través de PR (Pull Request), esto obliga a hacer todo un proceso de despliegue ya sea manual a automático antes de hacer cualquier lanzamiento a producción.
2. El branch del **pre-release-x.x.x**, este branch crea el nuevo número de versión en la que se trabaja para esa iteración, al finalizar la integración de los cambios hechos durante todo un periodo, este branch se encarga de unificar todo y es el último paso para llegar a master.
3. Existen n branches cortos llamados **pre-release-x.x.x.x-feature**, estos branches dinámicos son cada una de las funcionalidades que tiene el proyecto, si lo aterrizamos a Casos de Uso o Historias de Usuario, son las que tenemos dentro de la lista de Requerimientos.
4. Por último tenemos los branches **hotfix**, estos son derivados generalmente de **master** debido a que se encuentra un bug urgente a resolver que si aplicaramos todo el proceso de un nuevo release tomaría mucho tiempo, como el nombre indica, se hacen de manera rápida y no están pensados para ser mantenidos eternamente, de hecho lo que se busca es corregir con un parche rápido, y dentro de la siguiente iteración, corregir correctamente el error en un release normal.

Con esto ya vimos el uso del changelog y la estructuración de los branches para un buen gitflow, pero vamos a ponerlo en práctica.

## Paso 6 Plantilla PR

Una de las ventajas que nos ofrece GitHub, es poder agregar cosas para mejorar el proceso colaborativo.

Vamos a crear una plantilla que establezca lo que cada miembro del equipo debe cumplir para que se pueda aprobar un Pull Request.

Para ello dentro de nuestro proyecto vamos a crear una carpeta llamada **.github** y a esta vamos a añadirle un archivo llamado **PULL_REQUEST_TEMPLATE.md**

A este archivo vamos a añadirle lo siguiente.

```
<!--- Provide a general summary of your changes in the Title above -->

## Where can I try this functionality?
<!--- Please explain how this functionality can be accessed -->

## Types of changes
<!--- What types of changes does your code introduce? Put an `x` in all the boxes that apply: -->
- [ ] Bug fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)

## Checklist:
<!--- Go over all the following points, and put an `x` in all the boxes that apply. -->
- [ ] I have updated `CHANGELOG.md` accordingly.
- [ ] I have determined that these changes have no impact which
      have to be discussed with customers before deploying this feature.
      If in doubt, ASK.
- [ ] Another developer has performed a code review on this PR and approved it
- [ ] I have updated the related  cards in backlog, and will move this to "done" after
      merge & deploy.
```

Para ir acorde, voy a renombrar Changelog a CHANGELOG.

![graficas](/graphics/assets/img/lab4/22_lab4.png)

Como sigo trabajando en main, voy a actualizar mi changelog para poder subirlo

Hacemos commit y subimos al repositorio.

![graficas](/graphics/assets/img/lab4/23_lab4.png)

## Paso 7 Creando una iteración

Ahora vamos a empezar una nueva iteración del proyecto, lo primero que haremos será crear el branch para la siguiente versión.

```
git checkout -b pre-release-0.0.1

git push --set-upstream origin pre-release-0.0.1
```
![graficas](/graphics/assets/img/lab4/24_lab4.png)

Con esto tenemos nuestro nuevo branch desplegado.

Desde aquí cada miembro del equipo puede pocisionarse desde este branch y empezar a crear sus propios branches para poder trabajar.

Consideremos 2 casos de uso, el primero donde se necesita seguir crean cambios a **North Area** y el otro donde se necesita expandir la **South Area** del proyecto de Unity.

Entonces vamos a crear 2 branches que salen de el branch que acabamos de crear.

Antes que nada vamos a actualizar la entrada del changelog para indicar la nueva versión.

```
## [0.0.1] - UNRELEASED

### Added

### Changed

### Deprecated

### Removed

### Fixed

### Security
```

![graficas](/graphics/assets/img/lab4/25_lab4.png)


Guardamos, hacemos commit y lo subimos al repositorio al branch de pre-release.

![graficas](/graphics/assets/img/lab4/26_lab4.png)

Ahora si creamos nuestros 2 nuevos branches.

```
git checkout -b "pre-release-0.0.1.1-north-area"
git push --set-upstream origin pre-release-0.0.1.1-north-area

git checkout pre-release-0.0.1

git checkout -b "pre-release-0.0.1.2-south-area"
git push --set-upstream origin pre-release-0.0.1.2-south-area
```

Primero creamos el del caso de uso de la **North Area**, luego nos repocisionamos en el pre-release para partir desde ahí, y creamos el segundo branch.

![graficas](/graphics/assets/img/lab4/27_lab4.png)

Ahora nos vamos a colocar nuevamente en **pre-release-0.0.1.1-north-area**

```
git checkout pre-release-0.0.1.1-north-area
```

Vamos a Unity, y vamos a agregar algunas cosas al prefab de North Area, aquí no me detengo mucho, solo te dejo mi resultado final, pero ojo el cambio es al prefab.

![graficas](/graphics/assets/img/lab4/28_lab4.png)

Salvamos, actualizamos el changelog y hacemos nuestro commit y push.

![graficas](/graphics/assets/img/lab4/29_lab4.png)

Ahora nos cambiamos al branch de **pre-release-0.0.1.2-south-area**.

```
git checkout pre-release-0.0.1.2-south-area
```
![graficas](/graphics/assets/img/lab4/30_lab4.png)

Si nos vamos a Unity, observemos que desaparecen las esferas como debería, ya que nos encontramos una versión atrás.

Lo importante de este gitflow es estar actualizados al branch de **pre-release-0.0.1** como de momento no hay cambios si hago un

```
pull origin pre-release-0.0.1
```

Significa que puedo trabajar sin problemas, entonces ahora vamos a actualizar el prefab de la south area.

Mi resultado es el siguiente.

![graficas](/graphics/assets/img/lab4/31_lab4.png)

Guardamos el proyecto, actualizamos el changelog, hacemos commit y subimos al repositorio.

![graficas](/graphics/assets/img/lab4/32_lab4.png)

Ahora que ya cada quien termino, vamos a unificar los cambios en pre-release creando un Pull Request.

![graficas](/graphics/assets/img/lab4/33_lab4.png)

Y en el siguiente paso mucho ojo, por que queremos que sea el branch **pre-release-0.0.1.1-north-area** el que se haga merge con **pre-release-0.0.1** verifica que no este al revés o en su defecto que este seleccionado **master** o **main**.

![graficas](/graphics/assets/img/lab4/34_lab4.png)

Si hasta este punto ya has trabajado con PR, conoces todo este proceso. Pero si nunca has trabajado con plantillas que es lo que añadimos en el paso anterior cuando creas el PR, verás un cambio.

![graficas](/graphics/assets/img/lab4/35_lab4.png)

Observa que tenemos la plantilla cargada de nuestro PR vamos a llenarla y añadir más detalles.

Un buen PR debe ayudar al equipo a ver en que se trabajo, por que se hizo, y cumplir con el proceso de desarrollo de software, el texto de mi PR, queda de la siguiente forma, ojo que los screenshots es la ruta que me genera github.

```
<!--- Provide a general summary of your changes in the Title above -->

## Where can I try this functionality?
<!--- Please explain how this functionality can be accessed -->
Este PR expande la sección del North Area dentro del proyecto, se tuvieron algunos conflictos para ubir las medidas, y se optó por el uso de esferas como medio alternativo. Se deja screenshot de antes de comenzar y despues de comenzar como referencia del cambio.

## Screenshots
| Antes   | Después  |
| ----- | ----------- |
| ![18_lab4](https://user-images.githubusercontent.com/3307690/201157916-9801c11a-816b-4b17-81bf-6082122c0967.png) |   ![28_lab4](https://user-images.githubusercontent.com/3307690/201157974-eb897dd3-7338-4389-b18e-527be831fae5.png) |


## Types of changes
<!--- What types of changes does your code introduce? Put an `x` in all the boxes that apply: -->
- [ ] Bug fix (non-breaking change which fixes an issue)
- [X] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)

## Checklist:
<!--- Go over all the following points, and put an `x` in all the boxes that apply. -->
- [X] I have updated `CHANGELOG.md` accordingly.
- [X] I have determined that these changes have no impact which
      have to be discussed with customers before deploying this feature.
      If in doubt, ASK.
- [X] Another developer has performed a code review on this PR and approved it
- [X] I have updated the related  cards in backlog, and will move this to "done" after
      merge & deploy.
```

Y así el preview, me queda de la siguiente manera.

![graficas](/graphics/assets/img/lab4/36_lab4.png)

Ahora si le damos clic en **Create pull request** y aplicamos el proceso que tenga el equipo para la validación de los mismo que por lo general es el Code Review y en algunos casos pruebas manuales para ver que funcione todo correctamente.

Como de momento soy el unico trabajando en el proyecto, no puedo hacer ese paso, pero asumamos que ya se verifico el código por parte de alguien más.

Cerraremos el PR haciendo **Merge pull request** y por último **Confirm merge**

![graficas](/graphics/assets/img/lab4/37_lab4.png)

Finalmente eliminamos el branch ya que no se volverá a tocar

![graficas](/graphics/assets/img/lab4/38_lab4.png)

Si me voy al **pre-release-0.0.1** veo que mis cambios surtieron efecto y en los branches solo me quedan 3.

![graficas](/graphics/assets/img/lab4/39_lab4.png)

Ahora vamos a asumir que soy **pre-release-0.0.1.2-south-area** y que quiero juntar mis cambios a **pre-release-0.0.1**, si estoy siguiendo las buenas prácticas no voy a crear el PR inmediatamente, sino que primero voy a verificar que no haya cambios en **pre-release-0.0.1**, entonces nuevamente ejecuto.

```
git pull origin pre-release-0.0.1
```

Y ahora voy a ver que tengo algunos conflictos por resolver, en el caso particular el CHANGELOG. En general los conflictos a resolver deben ser simples, si se extiende a algo complejo, significa que **pre-release-0.0.1.1-north-area** no hizo bien su proceso.

Ahora si reviso el conflicto tengo lo siguiente.

![graficas](/graphics/assets/img/lab4/40_lab4.png)

Es en cierto modo obvio que esto sucede, entonces solo vamos a arreglar el conflicto ordenando el changelog para que quede como debería.

Justo aquí es donde depende la convención que tenga el equipo de acomodar por orden ascendente o descendente los cambios que van realizando, si son del mismo día igualmente deben decidir como se resolverían estos conflictos

![graficas](/graphics/assets/img/lab4/41_lab4.png)

Y solo por curiosidad nos vamos a Unity y veamos como se actualizan los objetos de manera automática, sin conflictos del proyecto.

![graficas](/graphics/assets/img/lab4/42_lab4.png)

Ya que tenemos todo nuevamente hacemos nuestro commit a **pre-release-0.0.1.2-south-area**

![graficas](/graphics/assets/img/lab4/43_lab4.png)

Ya qu eestmoa seguros que estamos con los últimos cambios de **pre-release-0.0.1** entonces ahora sí vamos a crear nuestro nuevo PR.

![graficas](/graphics/assets/img/lab4/44_lab4.png)

Llenamos nuestra plantilla del PR, con los datos correspondientes y tendremos un Preview como este.

![graficas](/graphics/assets/img/lab4/45_lab4.png)

Finalmente ejecutamos nuestro proceso de revisión, y una vez que todo este listo procedemos a hacer **Merge Pull request**, no olvides eliminar el branch.

![graficas](/graphics/assets/img/lab4/46_lab4.png)

Con esto ya tenemos solo 2 branches y nuestros cambios están unificados a **pre-release-0.0.1**.

### **Paso 8 Lanzando a producción**

Ya que todo está unificado vamos a hacer los últimos cambios en **pre-release-0.0.1** para poder unirlo a **main**.

Dentro de nuestra computadora vamos a colocarnos en el branch y vamos a bajar los cambios.

```
git checkout pre-release-0.0.1

git pull origin
```

No deberiamos tener ningún problema. Ahora vamos al changelog y actualiamos la fecha de lanzamiento y eliminamos las etiquetas que no utilizamos quedando de la siguiente forma.

```
# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.0.1] - 10/11/2022

### Added
- Se actualiza South Area, se agregan cilindros (10/11/2022).
- Se actualiza North Area y se añaden esferas. (10/11/2022).

## [0.0.0] - 10/11/2022

### Added 

- Commit inicial del proyecto (10/11/2022).
- Primer commit del proyecto (10/11/2022).
- Actualización inicial de la escena (10/11/2022).
- Creación de prefabs (10/11/2022).
- Update North Prefab (10/11/2022).
- Se agrega el changelog al proyecto (10/11/2022).
- Se agrega plantilla para PR (10/11/2022).
```

Ya que tenmos este resultado vamos a ver que el changelog  para la versión 0.0.0 se hizo muy largo por no tener estructura adecuada.

Para la versión 0.0.1 se hizo muy puntual en cuales casos de uso se trabajaron, y si quisiera irme a más detalle puedo entrar al historia de PR e ir siguiendo según la versión el histórico, esto me ayuda a tener documentación completa sin haber tenido que construir más allá de un proceso de desarrollo de software.

![graficas](/graphics/assets/img/lab4/47_lab4.png)


Si me voy a Unity se debería ver con todos los cambios integrados como el último screnshot.

![graficas](/graphics/assets/img/lab4/48_lab4.png)

Guardamos todo, hacemos commit y subimos al repositorio.

![graficas](/graphics/assets/img/lab4/49_lab4.png)

Ahora vamos a crear el PR para unificar **pre-release-0.0.1** en **main**.

![graficas](/graphics/assets/img/lab4/50_lab4.png)

Podrá parecer que ahora llenar la plantilla es un poco redundante, pero en este caso vamos a unificar los cambios como un todo, y ojo el título del PR, lo modificaremos a que sea **Release 0.0.1**.

![graficas](/graphics/assets/img/lab4/51_lab4.png)

Creamos nuestro pull request y ahora en el proceso no debemos ejecutar nuevamente los Code Review, puesto que en teoría ya se hicieron, ahora se puede implementar pruebas con usuarios finales para ver que la versión sea estable y candidata a release, si se tienen pruebas automáticas y pruebas de ambiente se ejecutan en esta fase para asegurar que no rompamos main.

Finalmente hacemos el **Merge pull request** y eliminamos el branch.

El resultado es un repositorio con solo el branch de **main** pero con la nueva versión actualizada.

![graficas](/graphics/assets/img/lab4/52_lab4.png)

Si me voy al historial de commits, veremos todo el largo que seguimos durante una iteración.

![graficas](/graphics/assets/img/lab4/53_lab4.png)

Si aprendes a hacer este flujo evitarás usar comandos complejos de GitHub.

### **Paso 9 Creando un release desde GitHub**

El último paso que necesitamos es formalizar nuestro release dentro de GitHub, para ello vamos a hacer lo siguiente.

Dentro de nuestra computadora nos colocaremos en main o master, en mi caso main.

```
git checkout main

git pull origin
```

Ahora vamos a crear un **tag** para nuestra versión.

```
git tag -a v0.0.1
```

Esto nos abrirá una ventana para insertar información, a manera de tipo commit, lo común es agregar lo que tenemos en el changelog para mantener unicidad.

![graficas](/graphics/assets/img/lab4/54_lab4.png)


Una vez agregado el texto vamos a ejecutar el comando

```
git push origin v0.0.1
```

Si regresamos a GitHub veremos en la parte de Release que se añade un contador a nuestra etiqueta.

![graficas](/graphics/assets/img/lab4/55_lab4.png)


Si entramos a la etiqueta veremos lo siguiente.

![graficas](/graphics/assets/img/lab4/56_lab4.png)

Así si necesitamos obtener alguna versión para probar o para regresar en caso de ser necesario congelamos la versión disponible.

Ahora esto es apenas una etiquta, ahora vamos a GitHub.

![graficas](/graphics/assets/img/lab4/57_lab4.png)

Seleccionamos el crear un **New Release** y desde las opciones veremos que podemos agregar un tag ya creado. Vamos a seleccionar el que acabamos de crear.

![graficas](/graphics/assets/img/lab4/58_lab4.png)

Nuevamente llenaremos el título y la descripción con las notas del changelog.

![graficas](/graphics/assets/img/lab4/59_lab4.png)

Damos clic en **Publish release** y listo tenemos un nuevo release liberado.

![graficas](/graphics/assets/img/lab4/60_lab4.png)

Y observa como en el dashboard principal se actualiza nuestra versión.

![graficas](/graphics/assets/img/lab4/61_lab4.png)

Con esto podemos dar por finalizado todo nuestro proceso de organización, administración y trabajo colaborativo de nuestro proyecto.

Si tienes duda de alguno de los pasos, o aún no te sientes familiarizado con alguno de los conceptos de Git, acercate con tus profesores.

## Comentarios Adicionales

1. No olvides hacer un desarrollo en GitHub orientado a Gitflow para desarrollar en base a funcionalidades, cada branch debe ser un feature, y no olvides tener reuniones de integración para evitar conflictos.
2. Los conflictos del repositorio se dan por cambios en muchos días de trabajo, busca iteraciones cortas e incluso si puedes implementa una metodología de Administración de Proyectos para mayor control.
3. Crea plantillas para tus Pull Requests, GitHub, te permite crear plantillas donde especifiquen como equipo cual debe ser el proceso que necesitan seguir desde análisis, diseño, implementación y pruebas, para que una funcionalidad sea aprobada. El tiempo que tienen es poco pero si se dan un tiempo para definir esto van a hacer más eficiente su desarrollo.
4. No olvides lo que has aprendido hasta este punto en la carrera.