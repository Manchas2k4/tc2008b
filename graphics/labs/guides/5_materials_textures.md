# Materiales y Texturas

## Objetivo
En este laboratorio exploraremos el uso de materiales, texturas y otros elementos básicos de gráficas computacionales que hasta ahora solo hemos utilizado pero es importante conocer su funcionamiento.

## Instrucciones
Sigue los pasos descritos en la siguiente práctica, si tienes algún problema no olvides que tus profesores están para apoyarte.

## Laboratorio
### Paso 1 Crear un nuevo proyecto

Hasta ahora lo que hemos visto es que podemos crear un proyecto rápidamente sin preocuparnos mucho por los tipos, más que haciendo solo la diferencia entre proyectos 2D y 3D.

Ahora vamos a expandir un poco lo que hemos visto. Desde el **Unity Hub** crearemos un nuevo proyecto.

![graficas](/graphics/assets/img/lab5/1_lab5.png)

Al momento de crear un proyecto, si has seguido las instrucciones como hasta ahora, debes haber seleccionado el **3D core**.

![graficas](/graphics/assets/img/lab5/2_lab5.png)

Vamos a centrar nuestra atención un momento en los siguientes elementos que deben aparecer un poco más abajo.

![graficas](/graphics/assets/img/lab5/3_lab5.png)


Con lo que aprenderemos el día de hoy notaremos que incluso las demás plantillas ya cuentan con la optimización según la plataforma a la que van dirijidas. A diferencia de otros IDEs donde cambiar la plantilla solo nos da elementos de configuración para el proyecto. En Unity estas plantillas escalan un poco más ajustando configuraciones para los gráficos que queremos manejar.

1. El 3D, que es el que hemos utilizado hasta ahora es el estándar, y este a su vez contiene una configuración de luces y materiales estándar, esto quiere decir que muchos de los assets que bajemos de la tienda estarán preparados para este tipo de proyectos.
2. Luego tenemos el 3D (HDRP), esto significa High Definition Render Pipeline, es una plantilla preparada para gráficos de la más alta gama.
3. Por último tenemos el 3D (URP), el cual está más alineado a proyectos de desarrollo móvil o algo del estilo.

Es importante conocer la diferencia por el tema de materiales, ya que la configuración para cada uno se da de manera diferente.

Si te ha tocado, y si no lo veremos más adelante, existen algunos objetos que al importarlos tienen una especie de color rosado, esto se debe a que sus materiales no cuentan con la definición adecuada para ese Render Pipeline correspondiente.

Para iniciar crearemos el proyecto 3D normal como siempre para hacer el laboratorio.

### Paso 2 Importar asset

![graficas](/graphics/assets/img/lab5/4_lab5.png)

Mientras se crea el proyecto vamos a ir preparando, bajando el siguiente [asset](https://assetstore.unity.com/packages/3d/environments/urban/lowpoly-holiday-house-95243).

![graficas](/graphics/assets/img/lab5/5_lab5.png)

Vamos a importar todo lo que viene del asset.

![graficas](/graphics/assets/img/lab5/6_lab5.png)

![graficas](/graphics/assets/img/lab5/7_lab5.png)

Ya que importamos nuestro asset, vamos a navegar a su carpeta de prefabs y vamos a agregarlos a la escena.

![graficas](/graphics/assets/img/lab5/8_lab5.png)

Por último vamos a eliminar todo lo que no pertenezca a la casa.

![graficas](/graphics/assets/img/lab5/9_lab5.png)

![graficas](/graphics/assets/img/lab5/10_lab5.png)

Ahora voy a ajustar el layout de mi Unity para tener la siguiente visión en la escena para que me sea más fácil revisar lo que estoy haciendo.

![graficas](/graphics/assets/img/lab5/11_lab5.png)

Regresando al tema de materiales notaremos que la casa se ve bien, no tenemos ningun asset o parte de la casa en rosa, y esto es por que los materiales que tenemos cargan exactamente en nuestra plantilla según su configuración.

Vamos a dar un poco más de luz a la casa para ver mejor los cambios que vayamos haciendo, en primer lugar vamos a duplicar la **Directional Light** con **ctrl+d**.

![graficas](/graphics/assets/img/lab5/12_lab5.png)

Después vamos a rotar de manera arbitraría esa luza para que se note mejor lo que estamos trabajando, este paso no es necesario pero trabaja un poco apuntando las luces para que te familiarices.

![graficas](/graphics/assets/img/lab5/13_lab5.png)

### Paso 3 Materiales

Como ya hemos visto, un asset en Unity contiene varias partes según como este estructurado. En el caso del que acabamos de importar notaremos que el prefab contiene todas sus partes, ventanas, puertas, barandilla, palmera, la base, etc.

![graficas](/graphics/assets/img/lab5/14_lab5.png)

Si seleccionamos alguno de los componentes de la casa, veremos que en el **Inspector** estos contienen al menos un **Mesh Filter** y un **Mesh Renderer**.

![graficas](/graphics/assets/img/lab5/15_lab5.png)

Y a su vez observemos que cada **Mesh Renderer** tiene su elemento de Material añadido.

![graficas](/graphics/assets/img/lab5/16_lab5.png)

Igualmente, si vemos la mayoría de las veces por estandarización el material recibe el mismo nombre hacia el elemento al que está siendo aplicado, esto resulta obvio ya que al tener tantos elementos armados será difícil administrarlos cuando sean muchos.

Si seleccionamos el material veremos que en la carpeta de assets nos lleva directamente al material seleccionado.

![graficas](/graphics/assets/img/lab5/17_lab5.png)

Si seleccionamos el material desde assets veremos que tiene solo un shader **Diffuse**, un color o una textura. Sí sabes más de materiales sabrás que puedes configurar muchas cosas más. No es alcance del curso ver estos detalles, nosotros nos iremos por la línea más básica.

![graficas](/graphics/assets/img/lab5/18_lab5.png)

### Paso 4 Creando materiales

Dentro de nuestra carpeta de assets vamos a crear una llamada **Materials**.

![graficas](/graphics/assets/img/lab5/19_lab5.png)

Ahora vamos a crear un Material, dentro de nuestra nueva carpeta, al igual como hemos creado otros elementos es con **clic derecho** y desde el panel de **create** seleccionamos **Material**.

![graficas](/graphics/assets/img/lab5/20_lab5.png)

De nombre le pondremos **White**.

![graficas](/graphics/assets/img/lab5/21_lab5.png)

Ahora veremos que en el **Inspector** se ve un poco diferente, y esto es por que es un Material Estándar de Unity, y es que los que ya vienen del asset que importamos ya están optimizados al menos para la parte móvil. Pero al menos un material normal de Unity se ve como el que acabamos de crear.

![graficas](/graphics/assets/img/lab5/22_lab5.png)

Aquí podemos agregar texturas, elementos de metal, smooth, etc. De momento lo dejaremos como está.

Ahora vamos a sustituir los materiales de la casa con lo que acabamos de crear. Selecciona todos los elementos de la casa hacinedo clic y manteniendo la tecla **shift**.

![graficas](/graphics/assets/img/lab5/23_lab5.png)

Ahora en el **Inspector** en la sección de materiales seleccionaremos la opción.

![graficas](/graphics/assets/img/lab5/24_lab5.png)

Esto nos permitirá asociar un material para todos los elementos, selecciona **White** que es el que acabamos de crear.

![graficas](/graphics/assets/img/lab5/25_lab5.png)

Al seleccionarlo, observa como cambia toda la casa no solo de color, sino de textura.

![graficas](/graphics/assets/img/lab5/26_lab5.png)

Esto se ve más como si el asset estuviera en modelación. Con esto vamos a hacer una prueba seleccionando desde assets nuestro material **White**.

Si desde el **Inspector** modificamos el color, se modificará el color de todo el material.

![graficas](/graphics/assets/img/lab5/27_lab5.png)

Esto es una forma de generar materiales si no quieres tener texturas, juegos de muy baja definición solo cargan este tipo de materiales para ahorrar uso de recursos, obviamente esto hace que la definición del juego sea muy sencilla.

Regresando el material a blanco prueba a crear un nuevo material de un color diferente y asignaselo a algunos elementos de la casa.

El resultado es como el siguiente.

![graficas](/graphics/assets/img/lab5/28_lab5.png)

Ahora vamos a eliminar este nuevo material, en mi caso **Red** que acabamos de crear. Al hacerlo vamos a ver lo que te decía al inicio del color rosa.

![graficas](/graphics/assets/img/lab5/29_lab5.png)

Como ya puedes imaginarte este color rosa aparece por que estos dos elementos no contienen un material seleccionado, por lo que Unity nos forma el modelo pero realmente no se está renderizando. Cuando trabajamos con las diferentes plantillas, si un objeto no está optimizado para la configuración del proyecto esto es lo que nos empezará a suceder.

Para solucionarlo basta con asignar algún material, en este caso vamos a reasignar el blanco.

![graficas](/graphics/assets/img/lab5/30_lab5.png)

### Paso 5 Texturas

Ahora vamos a ver uno de los materiales que ya tiene el asset que importamos.

![graficas](/graphics/assets/img/lab5/31_lab5.png)

Y vamos a ver que en el caso de este material no tiene un color asignado, sino que tiene una textura.

En este caso vamos a observar que una textura no es más que una imagen las cuales están contenidas en su propia carpeta **Textures**.

![graficas](/graphics/assets/img/lab5/31_lab5.png)

![graficas](/graphics/assets/img/lab5/32_lab5.png)

Si abrimos la imagen, notaremos que no es más que eso, y su alguna vez ensamblaste juguetes con stickers verás que es prácticamente lo mismo o la misma idea.

![graficas](/graphics/assets/img/lab5/33_lab5.png)

Lo que sucede con las texturas es que al funcionar como etiquetas o stickers, se adhieren al material que a su vez se adhiere al modelo y si está bien hecho se acomoda justo como debería en proporciones como si estuvieramos pegando encima del objeto la imagen ajustandola en 3D.

Si abrimos la palmera podemos notar como se contienen los elementos que la contienen.

![graficas](/graphics/assets/img/lab5/34_lab5.png)

Y en su defecto observa el modelo 3D, como se van acoplando cada una de las partes, intenta identificar la imagen.

![graficas](/graphics/assets/img/lab5/35_lab5.png)

### Paso 5 Creando texturas

Ahora para manejar texturar en Unity, vamos a irnos a nuestro material **White**.

![graficas](/graphics/assets/img/lab5/36_lab5.png)

Si seleccionamos alguno de los que nos aparecen, observa que sucede con la casa.

![graficas](/graphics/assets/img/lab5/37_lab5.png)

Y esto nos añade a nuestro material que está añadido a cada uno de los elementos que conforman nuestro modelo y esto da el resultado.

![graficas](/graphics/assets/img/lab5/38_lab5.png)

Obviamente como nuestro material está asignado a todas las partes, ahora todo incluyendo las plantas, las ventans y las puertas toman la textura que asignamos al material.

Esto nos deja más que en claro que si queremos detallar cada parte, necesitamos crear una textura para cada uno de los elementos del juego.

**Nota: Visualizando un juego moderno piensa la cantidad de tiempo invertido en la creación de modelos, materiales y texturas, una gran parte del desarrollo se da justo en esta parte, otra parte se da en ensamblar cada cosa como elemento como lo hacemos en Unity, y al final asignar a cada cosa su comportamiento a nivel de programación es otra fase, por eso el tiempo de desarrollo en general es largo sobretodo si es un juego que va a hacer alguna inovación importante en el ámbito.**

¿Qué otras cosas podemos modificar? Mueve las demás propiedades de la casa como el **Metallic** o el Smoothness** También observa que estas pueden agregar sus propias texturas, estos ya son puntos más avanzados, lo mínimo es intentas que se tenga una textura base.

Ahora intentemos aumentar el Tilling, y disminuirlo.

Si lo aumentamos observa que sucede.

![graficas](/graphics/assets/img/lab5/39_lab5.png)

Si lo disminuimos observa que sucede.

![graficas](/graphics/assets/img/lab5/40_lab5.png)

Esto pasa tanto para el EjeX como para el EjeY. Esto nos sirve para cuando bajamos texturas de internet y necesitamos ajustarlas a nuestros objetos.

Vamos a eliminar el **Building_10** de la escena.

![graficas](/graphics/assets/img/lab5/41_lab5.png)

Y vamos a volver a agregarlo desde nuestros prefabs importados a la escena para recuperar sus materiales y texturas originales.

![graficas](/graphics/assets/img/lab5/42_lab5.png)

### Paso 5 Proyecto 3D (HDRP)

**Nota: No pierdas el proyecto actual ya que lo usaremos más adelante.**

Por ahora vamos a crear un nuevo proyecto pero ahora usando el **3D (HDRP)**.

![graficas](/graphics/assets/img/lab5/43_lab5.png)

Y nuevamente procederemos a añadir nuestro asset de la casa, justo los mismos pasos de añadirlo al proyecto y añadirlo a la escena.

Si te pide convertir los assets de la plantilla a HD, puedes cancelar o cerrar la ventan, pues lo que haremos será muy simple.

Pero ahora vamos a ver lo siguiente como resultado.

![graficas](/graphics/assets/img/lab5/44_lab5.png)

Como ya mencionamos, al no estar preparados los assets de materiales y texturas para el High Definition Render Pipeline, entonces estos no se cargan en el objeto pareciendo que no se tienen los mismo para la casa.

Para al menos poder observar la casa, lo que vamos a hacer es vamos a seleccionar todos los materiales.

![graficas](/graphics/assets/img/lab5/45_lab5.png)

Y en el Shader, vamos a modificarlo por **HDRP >> Lit**.

![graficas](/graphics/assets/img/lab5/46_lab5.png)

![graficas](/graphics/assets/img/lab5/47_lab5.png)

Con esto podremos al menos visualizar nuestro objeto y tener al menos una configuración estándar.

![graficas](/graphics/assets/img/lab5/48_lab5.png)

Ahora el trabajo que quedaría es agregar a cada elemento su textura.

Para **Airing** sería lo siguiente.

![graficas](/graphics/assets/img/lab5/49_lab5.png)

Ahora vamos a añadir el **Wall_clumb** que son las plantas en la ventana de la casa.

![graficas](/graphics/assets/img/lab5/50_lab5.png)

Y ahora observa como aunque la textura se asigna bien, se ve un poco rara. Vamos a modificar en el **Inspector** el **Surface Type** de Opaco a Transparente.

![graficas](/graphics/assets/img/lab5/51_lab5.png)

Para finalizar asigna cada uno de las texturas faltantes para completar la casa.

**Nota: Recuerda que en la sección de recursos del laboratorio te dejo algunas páginas para obtener materiales y texturas para tus proyectos**.

### Paso 6 Package Manager

Ahora vamos a cerrar nuestro proyecto HDRP, y vamos a regresar al tradicional de 3D.

Ya no vamos a utilizar la casa por lo que puedes borrarla de la escena. En su defecto si quieres mantener la configuración del proyecto te invitaría a crear uno nuevo pero eso lo dejo a tu criterio.

Ahora bien, hasta ahora hemos estado trabajando con los Assets de la tienda de Unity, sin adentrarnos mucho en el Package Manager.

Como ya sabrás esté nos ayuda a administrar los paquetes que descargamos, y no solo para assets en general, sino también para extensiones de Unity que pueden ayudarnos en nuestros desarrollos.

Para abrirlo nos vamos a **Window>Package Manager**y de ahí vamos a buscar **ProBuilder**. Asegurate que el filtro este colocado para todos los assets de Unity y no solo los que has descargado.

![graficas](/graphics/assets/img/lab5/52_lab5.png)

Vamos a instalar el ProBuilder y de manera directa veremos en nuestros Packages que se agregar al proyecto.

![graficas](/graphics/assets/img/lab5/53_lab5.png)

Ahora vamos a abrir la ventana del ProBuilder desde **Tool>ProBuilder>ProBuilderWindow**.

![graficas](/graphics/assets/img/lab5/54_lab5.png)

Ahora vamos a arrastrar la nueva ventana debajo de nuestra jerarquía pero arriba de nuestros assets.

![graficas](/graphics/assets/img/lab5/55_lab5.png)

Por último vamos a cambiar la visualización a usar Iconos, esto para hacerlo un poco más ad hoc a los programas de diseño.

![graficas](/graphics/assets/img/lab5/56_lab5.png)

El resultado final será como el siguiente.

![graficas](/graphics/assets/img/lab5/57_lab5.png)

Ahora vamos a seleccionar la opción **New Shape** y en las opciones adicionales seleccionaremos el cubo, por último en nuestra escena usando clic izquierdo arrastraremos según el tamaño que queramos y crearemos un cubo como se presenta a continuación.

![graficas](/graphics/assets/img/lab5/58_lab5.png)

El tamaño no es importante.

Para ver mejor lo que hacemos vamos a deshabilitar el skybox dando clic en la siguiente opción.

![graficas](/graphics/assets/img/lab5/59_lab5.png)

Algo importante a mencionar es que las primitivas creadas en ProBuilder son diferentes a las primitivas creadas desde Unity, si nos vamos al **Inspector** y vemos las opciones del cubo que acabamos de crear vemos algo como lo siguiente.

![graficas](/graphics/assets/img/lab5/60_lab5.png)

Prueba intentando crear otras primitivas.

Borraremos lo que hayamos creado y regresaremos a nuestro humilde cubito.

Ahora si bien tenemos las opciones de transformaciones normales de Unity, ProBuilder nos añade una opción para modificar los vértices de nuestras figuras.

![graficas](/graphics/assets/img/lab5/61_lab5.png)

Con esta opción seleccionada podemos ir a los vértices de nuestro cubo y modificarlos como lo necesitemos.

![graficas](/graphics/assets/img/lab5/62_lab5.png)

Las opciones adicionales nos permiten manejar los lados o las caras.

Intenta a experimentar un poco para que te familiarices con la herramienta.

Nota también que las figuras que agregamos traen por default el color blanco, este es el material que maneja ProBuilder al crearse.

Vamor a regresar a un cubo para poder hacer algunos otros ejercicios de modelado.

Una vez con el cubo vamos a seleccionar la opción **Subdivide Object** esto va a realizar una subdivisión de caras para el objeto añadiendo con cada clic el doble de lo que inicialmente tiene.

Teniendo el cubo seleccionado vamos a dar clic en la opción 2 veces para tener algo como lo siguiente.

![graficas](/graphics/assets/img/lab5/63_lab5.png)


Ahora usando la opción de las caras vamos a seleccionar al menos las que tenemos visibles como se muestra a cotninuación.

![graficas](/graphics/assets/img/lab5/64_lab5.png)

Ahora buscaremos dentro de las opciones de ProBuilder la que se llama **Extrude Faces**, vamos a dar algunos clics y observa lo que sucede.

![graficas](/graphics/assets/img/lab5/65_lab5.png)

Ahora si damos clic mientras presionamos la tecla **Alt** en el icono de ajustes del **Extrude Faces** podremos ajustar las opciones de distancia, prueba con 1.5 y ve la diferencia.

![graficas](/graphics/assets/img/lab5/66_lab5.png)

Vamos a deshacer los cambios a regresar a nuestro cubo original.

Ahora vamos a seleccionar una de las caras inferiores del cubo.

![graficas](/graphics/assets/img/lab5/67_lab5.png)

Y ahora seleccionaremos del menú de ProBuilder la opción **Select Face Ring**, observa como se selecciona toda la parte inferior del cubo. Ahora si hacemos **ctrl+E** veras como se aplica la opción **Extrude Faces**

![graficas](/graphics/assets/img/lab5/68_lab5.png)

![graficas](/graphics/assets/img/lab5/69_lab5.png)

Como toda herramienta, más que un tutorial por cada cosa necesitas practicarlo, experimentar y equivocarte.

Intenta hacer algunos experimentos puesto que la siguiente clase realizaremos nuestra actividad final del curso en 1 hora durante la clase.