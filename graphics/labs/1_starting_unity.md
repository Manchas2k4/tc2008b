# Principios básicos de Unity

## Objetivo
En este laboratorio exploraremos los principios del manejo de Unity como plataforma para el desarrollo de programas que utilizan interfaces gráficas. 

La mayor parte del contenido que veremos será enfocado al desarrollo 3D. Sin embargo puede que veamos algunos datos sobre el desarrollo 2D en el camino.

## Instrucciones
Sigue los pasos descritos en la siguiente práctica, si tienes algún problema no olvides que tus profesores están para apoyarte.

**Nota 1: Todo lo realizado tiene la misma aplicación ya sea Windos, Mac o Linux puede ser que algunos menús u opciones estén localizados en un lugar diferente al desplegado como referencia que es Windows**


**Nota 2: Este curso práctico inicial, esta basado en las guías iniciales de Unity Learning, si tienes alguna duda o quieres saber más al respecto revisa los tutoriales de Unity oficiales, tienen muy buena documentación al respecto y te permiten avanzar rapidamente en la plataforma**

## Laboratorio
### Paso 1 Crear un nuevo proyecto
Nosotros podemos crear un nuevo proyecto en Unity en cualquier lugar de nuestra computadora, si bien puede detectar alguna carpeta default, podemos sobreescribir este comportamiento y ajustarlo a donde nosotros queramos.

En primera instancia vamos a crear una carpeta nueva donde queramos guardar nuestro proyecto.

![graficas](/graphics/assets/img/1_lab1.png)

Ahora vamos a abrir Unity Hub y directamente veremos los proyectos que tenemos creados, para nuestro caso haremos lo siguiente.

![graficas](/graphics/assets/img/2_lab1.png)

En caso de que existieran más versiones de Unity instaladas al momento de dar click en crear proyecto aparecerán las correspondientes para seleccionar alguna.

![graficas](/graphics/assets/img/3_lab1.png)

**Nota Importante: Asegurate que tú y tu equipo tengán la misma versión ya que las diferencias empiezan a generar conflictos al momento de cargar y abrir sobretodo si es entre diferentes SO**

Una vez seleccionado el nuevo proyecto podremos ver que hay una gran cantidad de plantillas con las que podemos realizar un proyecto, en este caso nos vamos directamente con la opción 3D core.

![graficas](/graphics/assets/img/4_lab1.png)

Después no olvides modificar los datos del proyecto como lo es el nombre y la ruta con la carpeta que creamos inicialmente.

![graficas](/graphics/assets/img/5_lab1.png)

El nombre no es importante pero si quieres guardarlo como Lab1.

Si quieres poner otro nombre te daré un poco de contexto de que trata el laboratorio.

> Crearemos una escena con un vehículo el cual sigue una carretera de 2 carriles y a la cual iremos agregando diferentes obstáculos para ir evitándolos

Una vez con todo listo damos click en Crear Proyecto y esperamos a que empieze a generarse el proyecto. Ojo: La primera carga puede tomar un tiempo.

![graficas](/graphics/assets/img/6_lab1.png)
![graficas](/graphics/assets/img/7_lab1.png)

El resultado final será el editor listo para poder empezar a cargar nuestros archivos y poder empezar a trabajar como se muestra de la siguiente manera.

![graficas](/graphics/assets/img/8_lab1.png)

Igualmente si revisamos nuestra carperta del proyecto podremos ver los diferentes archivos que nos crea Unity por default para nuestro proyecto.
 
![graficas](/graphics/assets/img/9_lab1.png)

### Paso 2 Importando archivos básicos
Dentro de Unity podemos empezar a trabajar con formas básicas de elementos que ya trae por default la herramienta, o en su defecto primitivas básicas como cubos esfera y otros más.

Sin embargo, en un juego real, no vamos a usar lo básico o lo default para trabajar en un proyecto, muchos equipos de desarrollo tienen sus equipos de diseño ó en su defecto comprar los assets de terceros.

Lo importante aquí es manejar un estándar en el uso de: modelos, escenas, texturas, etc. Para poder trabajar.

**Nota: Siempre que trabajes con archivos externos revisa que Unity tenga la compatibilidad o en su defecto que puedas trabajarlos como los necesitas, he visto casos donde por mala perspectiva de los modelos es muy complicado estar trabajando con ellos**

Para el caso de este laboratorio solo necesitamos el archivo descargable que tienes a continuación. [Archivos Lab](/graphics/assets/Prototype%201%20-%20Starter%20Files.zip)

Al descargarlo notarás que es un archivo zip, el cual deberemos extraer su contenido a un lado de la carpeta en donde tenemos nuestro proyecto.

**Nota: Si bien no pasa nada al extraer la carpeta al proyecto por facilidad lo dejaremos a un lado para marcar que son archivos externos, ojo si manejas esta estructura en un repositorio ya que en cuyo caso deberas crear una carpeta padre contenedora, luego la del proyecto y a la par la que acabamos de agregar.**

![graficas](/graphics/assets/img/10_lab1.png)

Ahora regresaremos a Unity y desde el menú superior nos iremos a la opción de **Assets>Import Packages>Custom Package...**

![graficas](/graphics/assets/img/11_lab1.png)

Con esta opción deberemos seleccionar el archivo que viene dentro de la carpeta que descargamos y que colocamos a la par de nuestro proyecto, si lo vemos desde el explorador este sería el archivo.

![graficas](/graphics/assets/img/12_lab1.png)

Al agregarlo al proyecto, dentro de unity veras que te aparece la siguiente lista de opciones.

![graficas](/graphics/assets/img/13_lab1.png)

Lo importante a destacar aquí es que si bien puedes agregar modelos, texturas, sonidos y demás artefactos al proyecto de manera individual, existen estas carpetas ya preparadas que contienen librerías completas de assets, que tan completas esten depende de quien las haga y puedes verlo como sets completos con los que puedes hacer cosas, si bien es la forma ideal de trabajar con unity para obtener materiales, lo triste es que esto no siempre será así. Por ahora es lo único que necesitamos.

Da clic en Importar y espera a que se agregen los assets al proyecto.

Si pudiste notar al finalizar la importación se agrega una nueva carpeta a nuestro espacio de trabajo.

![graficas](/graphics/assets/img/14_lab1.png)

También notarás que hay varios warnings apareciendo debajo del editor, por el momento no deberían afectarnos así que podemos pasar de ellos.

![graficas](/graphics/assets/img/15_lab1.png)

Si los queremos quitar, damos clic en los warning y aparecerá lo siguiente, damos clic en clear y se eliminarán.

![graficas](/graphics/assets/img/16_lab1.png)

### Paso 3 Familiarizando los objetos

Para comenzar seleccionaremos la carpeta Scene de nuestro proyecto.

![graficas](/graphics/assets/img/18_lab1.png)

Y daremos doble click en la que se llama **Prototype 1**

![graficas](/graphics/assets/img/19_lab1.png)

Y veremos que al cargarse se abre de manera automática nuestra escena que contiene un mundo y como parte de ese mundo ya contiene nuestro camino de 2 carriles.

Uno de los puntos más importantes que deberás aprender sobre Unity es como poder moverte a través de las escenas, y esto para poder ajustarte donde tu lo necesitas en el proyecto.

Para empezar con algo simple muevete a través de la escena con tu mouse.

Si das clic izquierdo veras que intenta seleccionar cosas, si por error mueves algo puedez usar **ctrl+z**. Para movernos da clic derecho y empieza a maniobrar la cámara que tenemos de visibilidad. Notarás que no avanza, y esto es por el modo que tenemos seleccionado. Interactua un poco a que la pocisión quede de tal forma que te acomodes a ver lo más que se pueda de nuestro mundo.

![graficas](/graphics/assets/img/20_lab1.png)

Ahora bien, para continuar con nuestro trabajo, eliminaremos la escena Sample que tenemos en el proyecto, esto para evitar tener cosas que no vamos a utilizar.

![graficas](/graphics/assets/img/21_lab1.png)

Damos clic en la escena, después suprimir y aceptamos el mensaje de eliminarlo, como resultado tenemos que en nuestra carpeta **Scenes** solo está la escena del **Prototype 1**

Para continuar con la navegación, seleccionaremos nuestra escena nuevamente y ahora nos moveremos con **las flechas del teclado** para movilizar la cámara de un lado a otro. Esto en conjunto con el pocisionamiento del ratón usando el clic derecho nos permite maniobrar por todo nuestro mundo para poder movernos.

![graficas](/graphics/assets/img/22_lab1.png)

Si te mueves muy lejos de la base de la carretera con las flechas notarás algo muy importante en nuestro proyecto que tal vez ya sabías o habías escuchado en el mundo de los videojuegos.

Los mundos no son infinitos, tienen límites, y en este caso nuestro mundo es como una gran esfera que representa nuestra escena, siempre y cuando respetemos esos límites nuestro mundo usará la textura que estamos viendo en el editor.

Las escenas y sus elementos son espacios especiales que se crean en Unity para crear esta base de mundos, si hablamos de un juego donde hay varios niveles, necesitariamos crear estas geodas con los diferentes elementos que conformarían cada nivel en particular.

Con todo esto tenemos los elementos más básicos para poder trabajar en nuestro proyecto.

> Si te preguntas por que no modelamos toda la escena desde 0 esto tiene una razón muy sencilla, la primera es que el curso de estos laboratorios es para revisar físicas, movimientos y funcionalidades en Unity y no como tal modelado ya que es igualmente toda una área de aprendizaje. Por eso mismo utilizamos modelos que se pueden obtener incluso de manera gratuita en la tienda de Unity

**Nota: Si moviste algo, trata de regresarlo a su lugar con ctrl+z esto para evitar que vaya a haber problemas con lo que veremos más adelante.**

**Nota 2: Te invito a crear aparte un proyecto adicional usando lo mismo que hicimos hasta este punto, pero en ese si mueve todo lo que puedas hasta romper la escena si es necesario, así le tendrás menos miedo a moverle y ver como recuperarte de algún movimiento inesperado como pudiera existir en tu proyecto.**

## Paso 4 Agregando vehículos

En nuestro proyecto abriremos la carpeta de **Course Library** y de primera mano observemos que contamos con los diferentes elementos o bloques que podemos usar para hacer nuestro proyecto, de manera directa nos iremos a la carpeta de **Vehicles** y seleccionaremos la camioneta para empezar.

Para agregar un objeto podemos seleccionarlo y arrastrarlo a la escena, o en su defecto podemos dar doble clic, la diferencia entre uno y otro es que si lo arrastramos nosotros controlaremos donde aparecerá, si damos doble clic se pocisionará automáticamente en las coordenadas 0,0,0.

![graficas](/graphics/assets/img/23_lab1.png)

Si observamos no solo estamos agregando el objeto a la escena, sino también a la jerarquía del proyecto. Aquí es donde tendremos disponibles todos los elementos de nuestra escena.

![graficas](/graphics/assets/img/24_lab1.png)

Juega un poco y agrega todos los vehículos a la escena para que te familiarices con estos componentes, no olvides jugar con tu cámara para acomodarte en los lugares donde quieras acomodarlos.

![graficas](/graphics/assets/img/25_lab1.png)

Una vez que hayas experimentado completamente, borra todos los vehículos para dejar la escena como estaba inicialmente.

Ahora nuevamente agregaremos la camioneta que viene en la carpeta de vehículos para tene algo como lo siguiente.

![graficas](/graphics/assets/img/26_lab1.png)

Como nos hemos estado moviendo en la escena es con clic derecho y las flechas del teclado, pero vamos a hacerlo un poco más fácil.

Da clic derecho en la escena para poder moverte, pero en lugar de mover la mano con el mouse, utiliza las teclas W,A,S,D en forma que lo harías con las flechas del teclado y nota como se empieza a mover igualmente la cámara.

Ahora bien, por comodidad acomodaremos nuestro vehículo de la siguiente forma en la jerarquía y nos aseguraremos que este seleccionado.

![graficas](/graphics/assets/img/27_lab1.png)

Al seleccionarlo te darás cuenta que se selecciona el objeto y nos muestra como esta construido, esto se ve más al tipo de imágenes que nos presentan en el desarrollo de elementos 3D. Una forma de navergar rapidamente al elemento y centrarlo es utilizando la tecla **f** esto nos acerca a las coordenadas centrales donde se encuentra el objeto.

![graficas](/graphics/assets/img/28_lab1.png)

>Como ya mencionamos el curso no está orientado a diseño, pero algo importante que debes saber, es que si quieres dar detalle a los elementos es que cada uno debe ser un elemento independiente, piensalo como en bloques de lego, si te diera un carro ya hecho, se ve bien pero no puedo moverlo directamente puesto que todas las piezas son una misma, al contrario si te doy cada parte individual como las llantas, las ventanas e incluso si nos vamos a mayor nivel de detalle el motor, los tornillos, etc. Podemos llegar a un nivel de detalle muy amplio. El que tanto ya depende del juego en sí, y obviamente entre mayor nivel de detalle aumenta la carga que tenemos que ejecutar a la computadora para correr elementos, así que encontrar un nivel equilibrado entre elementos es la clave de buenos videojuegos. En clase veremos algunos trucos para hacer detalle sin que esto signifique matar la computadora a nivel de recursos.

**Nota: Al centrar elementos, nota que todos los objetos tienen un centro, este se llama el punto de anclaje, estos nos sirven para que al pocisionar el objeto este se acomode en las coordenadas que le decimos. Siempre, siempre, siempre cuida esto, a veces al modelar las personas pueden llegar a mover este punto de anclaje por decir en el caso de la camioneta, en vez del centro a la llanta, y esto cambía drasticamente la pocisión, si bien se puede trabajar así, necesitarías modificar todo el pocisionamiento, por lo que se recomienda colocar el punto de anclaje en un lugar que sea natural, por lo general el centro, para que tenga sentido el acomodo. No es tán visible solo describirlo, pero creeme que es un dolor de cabeza cuando sucede.**

Otros comandos para el manejo de nuestra cámara los podremos notar haciendo lo siguiente.

Si presionamos la tecla **Alt** y damos **clic izquierdo** podremos rotar la camara alrededor del elemento que tenemos seleccionado.

Si presionamos la tecla **Alt** y damos **clic derecho** podremos hacer zoom in o zoom out.

### Paso 5 Agregando Obstáculos

En base a lo que hicimos en el paso anterior, entra a la carpeta de **Obstacles** dentro de nuestro **Course Library** y nuevamente te invito a explorar, jugar y colorar los diferentes objetos de obstáculos que tienes a tu dispocisión.

Una vez que hayas explorado lo suficiente, borra todos los obstáculos que hayas agregado. Y para nuestro caso agregaremos una caja.

![graficas](/graphics/assets/img/29_lab1.png)

Como podrás observar, coloqué la caja adelante del carro, pero veamos como puedo pocisionar rapidamente un elemento en 0,0,0.

Me iré al inspector del lado izquierdo de Unity y buscaré la opción de **Transform.**

![graficas](/graphics/assets/img/30_lab1.png)

En esta opción daremos clic en los 3 puntitos y seleccionaremos reset.

![graficas](/graphics/assets/img/31_lab1.png)

Esto cambiará la pocisión de nuestra caja a 0,0,0.

![graficas](/graphics/assets/img/32_lab1.png)

El reset que seleccionamos, cambia toda la propiedad de transform, pero igualmente veremos que podemos hacer un reset solo a la pocisión, la rotación y la escala individualmente.

Ahora, vamos a esconder nuestra camioneta de la siguiente manera. Dentro de la jerarquía seleccionamos nuestra camioneta.

![graficas](/graphics/assets/img/33_lab1.png)

Después nos iremos al inspector y en la parte superior donde viene el nombre de nuestro objeto deseleccionaremos la opción.

![graficas](/graphics/assets/img/34_lab1.png)

Como resultado nuestra camioneta sigue estando en la escena pero estará oculta.

![graficas](/graphics/assets/img/35_lab1.png)

Ahora vamos a explicar un poco sobre los planos x,y,z. Pero primero para poder hacerlo vamos a acomodar nuestra cámara para poder explicarlo.

Notarás que en la escena tenemos una especio de cubo con pirámides, este nos permite pocisionar exactamente el plano según el eje seleccionado.

![graficas](/graphics/assets/img/36_lab1.png)

Vamos a dar click en el eje y que está en verde y la cámara se debe pocisionar como a continuación se muestra.

![graficas](/graphics/assets/img/37_lab1.png)

Ahora nos aseguramos que seleccionamos nuestra caja.

![graficas](/graphics/assets/img/38_lab1.png)

Y si puedes ver poniendo atención en el **Inspector** se puede mover la caja dando click en las flechas que aparecen encima de ella. 

Por ejemplo: Si muevo la flecha azul, empezaré a mover en el eje z, de hecho si miro según la alineación la flecha roja corresponde a las x y la verde que apunta hacia nosotros es el eje y.

![graficas](/graphics/assets/img/39_lab1.png)

> Puedes estarte preguntando, por que se tiene esta alineación, si lo ideal sería que el eje y y el eje z estén invertidos. La respuesta es que no hay una sola forma de hacerlo. Si bien lo ideal es maneralo así depende de como se modele la escena para seguir las coordenadas, por que incluso se podría inclinar o rotar para que no hiciera match con nada, obviamente esto haría más complejo el poder trabajarlo, por lo que normalmente con que se pueda alinear a los ejes sin importar el orden es suficiente.

Para finalizar coloca nuestra caja en la pocisión z en la coordenada 25. Debiendo quedar en 0,0,25.

![graficas](/graphics/assets/img/40_lab1.png)

Si habilitamos nuevamente la camioneta deberemos tener un resultado como el siguiente.

![graficas](/graphics/assets/img/41_lab1.png)

Con todo lo que hemos hecho hasta el momento notarás que el nombre en la jerarquía para nuestros objetos, es el que traen por default, de momento no afecta mucho, pero en juegos más grandes esto puede generar confusión.

Por lo tanto vamos a renombrar los elementos. Teniendo la camioneta seleccionada en el inspector modificaremos el nombre justo a un lado de la casilla para hacer visible o invisible el elemento, de nombre le pondremos **Vehiculo** y lo mismo para la caja le pondremos el nombre de **Obstaculo.**

![graficas](/graphics/assets/img/42_lab1.png)
![graficas](/graphics/assets/img/43_lab1.png)

El resultado será que en nuestra jerarquía podremos identificar más facilmente nuestro objetos.

![graficas](/graphics/assets/img/44_lab1.png)

### Paso 6 Modificando la cámara

Ahora vamos a empezar a hablar de uno de los elementos clave en cualquier proyecto, **la cámara.**

Hasta ahora nos hemos movido en nuestra escena con la cámara default, pero esto es solo en el modo de desarrollo que tenemos habilitado. Si puedes ver en la sección de la escena tenemos otro modo que es el de juego.

![graficas](/graphics/assets/img/45_lab1.png)

Ahora bien, antes de empezar a hablar del modo juego, veamos que tenemos otros elementos en nuestra jerarquía que son importantes.

En primer lugar tengo mi Main Camera, que como su nombre indica es lo que está viendo mi juego al ejecutarse. Notarás que aparecen las líneas y el icono de una cámara pero como podrás imaginar al momento de ejecutarse todo esto no se ve tal cual.

![graficas](/graphics/assets/img/46_lab1.png)

El segundo elemento que tenemos es el **Directional Light** que igualmente como su nombre indica nos ayudan a dar luz a nuestra escena. Juegos más complejos utilizan todo un set completo de luces diferentes para destacar elementos. Así como el modelado, las luces son toda un área de especialización completa.

![graficas](/graphics/assets/img/47_lab1.png)

Por último tenemos nuestro environment el cual como ya habíamos explicado nos da todo el mundo que tenemos.

![graficas](/graphics/assets/img/48_lab1.png)

Regresando al **game view** como mencionabamos esta vista es lo que vamos a ver cuando estemos jugando. Para habilitarlo va a ser el correspondiente a ejecutar nuestro proyecto y esto lo podemos hacer dando clic en el botón de play.

![graficas](/graphics/assets/img/49_lab1.png)

Esto puede tomar un momento, ya que requiere hacer la compilación para comenzar, sobre todo al inicio.

Como resultado tendremos lo siguiente.

![graficas](/graphics/assets/img/50_lab1.png)

Si ves el color de mi Unity es como azulado, en tu caso debe aparecer como grisaceo, no te preocupes, más adelante te diré como personalizar esto.

Lo importante ahora es que veas que esta seleccionada la vista de game y que la cámara que vemos es completamente diferente, incluso si intenamos movernos no será posible puesto que no hemos programado ningún tipo de movimiento en el juego tanto para nuestros objetos como para nuestra cámara.

Para detener el modo juego da clic nuevamente en el icono de play con esto Unity volverá a sus colores normales.

![graficas](/graphics/assets/img/51_lab1.png)

**Nota: Evita presionar el icono de pausa, este se utiliza en otros casos, puedes verlo como pausar el juego, pero es importante por que si das clic en pausa y modificas tus elementos, al detener el juego estos volverán a su estado original, por lo que corres el riesgo de perder tus cambios.**

Como podrás sospechar la vista de cámara esta directamente relacionada con el objeto **Main Camera** de nuestra jerarquía, y si lo seleccionamos y nos acomodamos un poco podemos observar lo siguiente.

![graficas](/graphics/assets/img/52_lab1.png)

La cámara cubre lo que se tiene en la **Main Camera** y las líneas que lo acompañan son la línea de visión que tienen.

Ahora, decimos que la cámara esta directamente relacionada a la **Game View** por que si movemos la cámara hacia la derecha, en el previsualizador, podemos empezar a ver nuestro obstáculo. Igualmente si empezaramos a jugar con la cámara podemos acomodarla en cualquier punto del juego.

![graficas](/graphics/assets/img/53_lab1.png)

Lo que haremos ahora será tratar de pocisionar la cámara detrás de nuestro vehículo a que quede más o menos de esta forma.

![graficas](/graphics/assets/img/54_lab1.png)

Para hacerlo intenta mover la cárama de forma manual para poder hacer todos estos movimientos. Esto para que puedas explorar todos estos elementos.

Para ayudarte vamos a ver como rotar la cámara puesto esta viendo de frente al vehículo y lo queremos desde atrás.

Pocisionamos la cámara en x=0,y=2,z=-5

Para rotarla usaremos las opciones de rotación de la escena, con nuestra cámara seleccionada haremos lo siguiente.

![graficas](/graphics/assets/img/55_lab1.png)

Al seleccionar está opción verá que cambia la línea de posición y se convierte en una esfera, siguiendo la misma idea de los ejes y sus colores podemos rotar nuestra cámara de forma manual.

Nuevamente antes de darte la respuesta te invito a experimentar un poco con las diferentes opciones de los ejes para que te familiarices un poco.

Ahora en la sección de **Rotation** del **Inspector** vamos a ajustar las coordenadas a x=0,y=0,z=0.

![graficas](/graphics/assets/img/56_lab1.png)

Vamos a terminar de ajustar un poco más la cámara terminando con los siguientes valores.

![graficas](/graphics/assets/img/57_lab1.png)

Si damos clic en play, y vamos a la  **Game View** veremos el resultado final de nuestra cámara.

![graficas](/graphics/assets/img/58_lab1.png)

### Paso 7 Layouts
Con lo que hemos hecho hasta ahora espero sientas un poco complicado estar trabajando con el inspector, las vistas, los assets y la jerarquía. Aunque esta es la forma default que trae Unity para trabajar es claro que conforme avancemos necesitemos de formas más optimas para desplazarnos.

Para esto nos sirven los **layouts** o plantillas, estas nos permiten modificar la forma en que acomodamos nuestro IDE.

![graficas](/graphics/assets/img/59_lab1.png)

Como puedes observar tenemos algunos predefinidos, observa los dierentes ajustes que podemos obtener.

![graficas](/graphics/assets/img/60_lab1.png)

![graficas](/graphics/assets/img/61_lab1.png)
![graficas](/graphics/assets/img/62_lab1.png)
![graficas](/graphics/assets/img/63_lab1.png)

La vista default es la que ya tenemos así que no es necesario agregarla.

Si bien todas estas visualizaciones diferentes podemos encontrar alguna que nos sirva, mejor vamos a optimizarla un poco más.

Tomando como base la de **Tall**, vamos a seleccionar la vista de juego y la vamos a arrastrar a la parte inferior.

![graficas](/graphics/assets/img/64_lab1.png)
![graficas](/graphics/assets/img/65_lab1.png)

Con esto tendremos nuestra vista de escena como mayor fuente, pero al ejecutar tenemos nuestra vista de juego y evitamos estar pasando de una a otra.


Ahora vamos a ir a la sección del proyecto y vamos a modificar la vista de carpetas que ocupan bastante espacio y la vamos a cambiar a una sola columna como se muestra.

![graficas](/graphics/assets/img/66_lab1.png)

El resultado será algo como lo siguiente.

![graficas](/graphics/assets/img/67_lab1.png)

Con esto modificamos nuestro layout para este proyecto, pero si queremos que esto se mantenga o incluso compartirlo o guardarlo para futuros proyectos lo podemos hacer de la siguiente manera.

![graficas](/graphics/assets/img/68_lab1.png)

La ruta de guardado puede ser donde sea, pero para mantener la administración, lo guardaremos en la carpeta que descomprimimos donde se incluye el pack de nuestro objetos del proyecto.

![graficas](/graphics/assets/img/69_lab1.png)

Y con esto si llegaramos a cambiar la plantilla, solo necesitamos volverla a cargar en  **Loa Layout from File** y esto regresará a como lo habíamos dejado.

### Paso 8 Primer Script

Para seguir con nuestro proyecto nos iremos a la sección del Proyecto y enla carpeta de assets crearemos un nuevo folder.

![graficas](/graphics/assets/img/70_lab1.png)

Como resultado nos aparecerá lo siguiente

![graficas](/graphics/assets/img/71_lab1.png)

Ahora procederemos a crear un nuevo script de la misma forma pero seleccionando lo siguiente.

![graficas](/graphics/assets/img/72_lab1.png)

Al archivo lo llamaremos **PlayerController**

Y el resultado será el siguiente.

![graficas](/graphics/assets/img/73_lab1.png)

Ahora seleccionaremos nuestro vehículo y vamos a observar el **Inspector**. Hasta ahora solo hemos trabajado con las opciones del **Transform** sin embargo vale la pena ver con que mas componentes cuenta nuestro objeto como son el **Mesh Filter**, el **Mesh Renderer** y el **Mesh Collider** que son los que le permiten a nuestro objeto ser un objeto.

Si seleccionamos los otros componentes de nuestra escena, veremos los diferentes componentes que lo conforman.

Entonces, en nuestra camioneta nos iremos a la opción de **Add Component** ó en su defecto desde la sección del proyecto podemos arrastrar nuestro PlayerController al objeto, quedando algo como lo siguiente.

![graficas](/graphics/assets/img/74_lab1.png)

Ahora los siguientes pasos van a depender de si instalaste visual studio o no. Si haces doble clic se intentará abrir visual studio para editar el código.

En mi caso yo estaré utilizando Visual Studio Code por lo que no habrá autocompletado.

Sin importar donde edites los scripts, al guardarlos Unity por default sabrá que hubo cambios y recargará los scripts para visualizarlos en el IDE y en su defecto cargarlos cuando corras el proyecto.

Si haces lo mismo que yo en cuestión de visualizar en Visual Studio Code u otro Editor de Texto, te recomiendo lo abras desde el explorador y jales desde ahora la carpeta de Scripts para que te sea más rápido visualizar todo.

**Nota: Existen algunos plugins para C# y Unity en Visual Studio Code, no te los recomiendo pues no son oficiales, son realizados por terceros y pudieran llegar a darte problema.**

![graficas](/graphics/assets/img/75_lab1.png)

Ahora vamos a revisar un poco el código que se genera de manera automática.

En primer lugar tenemos las librerías básicas de imports como lo tendriamos en otros lenguajes como C++,Java,Kotlin,etc.

```
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
```

Después tenemos la inicialización de nuestra clase y observaremos que está heredando de la clase MonoBehavior, de momento no entraremos en detalles de la sintáxis de C#, eso lo haremos un poco más adelante.

```
public class PlayerController : MonoBehaviour
```

Ahora, verás que tenemos varias funciones ya creadas, estas nos ayudan al ciclo de vida de nuestro juego, esto quiere decir que se ejecutan cada cierto momento durante la vida y ejecución de nuestra aplicación.

El método Start se ejecuta al momento de cargar nuestro juego, sirve por lo general para las configuraciones iniciales de nuestro juego.
```
void Start()
{
    
}
```

El método update como nos indica se ejecuta cada vez que se actualiza cada frame del juego, podemos verlo como un ciclo continuo dependiendo de las acciones que nosotros hacemos.
```
void Update()
{
    
}
```

Vamos a reflexionar un momento y piensa, si quisieramos hacer que nuestro vehículo avance, en que método lo haríamos.

Si mencionaste el update, es lo correcto, por ahora añadiremos solo un pequeño comentario.

```
void Update()
{
    //Mover vehiculo hacia adelante
}
```

Ahora, las clases que estaremos usando son todas las que ya vienen por default en el API de Unity, si tienes duda no dudes en consultarlo, la liga te la dejo aquí [Documentación Unity](https://docs.unity3d.com/Manual/index.html)

Lo primero que haremos será añadir la siguiente línea para decirle que se mueva en posición en 1 unidad, y recuerda que como el método update se llama en cada actualización de frame, esto es lo mismo que estar sumando 1 unidad de coordenadas cada vez. Para nuestro vehículo por lo que habíamos observado la carretera avanza en el sentido del eje z, por lo que ahí es donde modificaremos el valor.
```
void Update()
{
    //Mover vehiculo hacia adelante
    transform.Translate(0,0,1);
}
```

Intenta correr el juego y ve que es lo que sucede.

Si todo salió bien el carro sale volando y desaparece de la vista.

La línea de mover la pocisión ya vimos que nos funciona para poder trabajar, pero si quisieramos ahcer cambios más drásticos en las pocisiones necesitariamos declarar cada vez los ejes x,y,z.
```
transform.Translate(0,0,1);
```

Para evitar estar escribiendolo directamente, vamos a utilizar una clase por default de Unity llamada Vector3, que en este caso simula un Vector 3D, la teoría la veremos en clase, pero este vector permite manipular la magnitud en este caso de las coordenadas x,y,z de una manera más limpia y fácil. Así bien, nuestro código quedaría de la siguiente manera.

```
void Update()
{
    //Mover vehiculo hacia adelante
    //transform.Translate(0,0,1);
    transform.Translate(Vector3.forward);
}
```

Si ejecutamos nuevamente veremos el mismo resultado, el vehículo saliendo disparado hacia la nada.

De momento lo dejaremos por aquí, en el próximo laboratorio seguiremos ajustando los detalles como la velocidad, gravedar y manejo de nuestro vehículo.