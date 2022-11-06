# Prefabs y Multiplayer Local en Unity

## Objetivo
En este laboratorio extenderemos la funcionalidad del laboratorio anterior añadiendo objetos con comportamiento personalizados y configuraremos el proyecto a trabajar como un pequeño juego multiplayer local.

## Instrucciones
Sigue los pasos descritos en la siguiente práctica, si tienes algún problema no olvides que tus profesores están para apoyarte.

## Laboratorio
### Paso 1 Creando un prefab

Para comenzar, vamos a ocultar el Objeto de Obstáculos que creamos el día anterior.

![graficas](/graphics/assets/img/111_lab1.png)

Ya que limpiamos nuestra carretera, ahora vamos a proceder a crear pirámides, esto con los objetos que ya tenemos.

Ahora agregaremos una caja a nuestra jerarquía desde **assets>course library>Obstacles**

![graficas](/graphics/assets/img/112_lab1.png)

Después a esta misma caja, le agregaremos el componente de **rigidbody** y modificaremos su masa a 10.

![graficas](/graphics/assets/img/113_lab1.png)

El siguiente paso será crear un nuevo folder que se llame **Prefabs**.

![graficas](/graphics/assets/img/114_lab1.png)

Ahora arrastraremos nuestra caja desde la jerarquía hasta la carpeta de **Prefabs**, un mensaje como el siguiente deberá aparecer.

![graficas](/graphics/assets/img/115_lab1.png)

Seleccionaremos la opción de **original prefab** y el resultado final será que nuestra caja aparecerá en la carpeta.

![graficas](/graphics/assets/img/116_lab1.png)

Hacer esto es muy importante, puesto que nos permitirá realizar objetos personalizados, con el ejemplo que tenemos podemos ver lo siguiente.

Si agregamos una caja desde **course library>obstacles** agregamos el modelo, sin embargo estos modelos al ser los básicos no cuentan con un **rigidbody**.

Si agregamos ahora la caja pero desde nuestra carpeta de **Prefabs** nos daremos cuenta de que el **rigidbody** ya viene añadido y más aún el valor base que dejamos de 10 ya viene integrado.

Como resultado vemos que se pueden crear objetos con toda una personalización más allá del modelo básico y poder trabajar sobre ello.

Si aún no ves muy bien la diferencia entre uno y otro te invito a crear una caja desde **course library>obstacles** y usar tu carro para ir entre la que ya tenemos y la nueva para que veas la diferencia.

Ahora procederemos a crear nuestra pirámide de objetos. Utilizando el prefab que creamos, usaremos esta primera caja y la posicionaremos en:

- x = 2
- y = 0
- z = 12

![graficas](/graphics/assets/img/117_lab1.png)

Después duplicaremos la caja ya sea agregando otro prefab o duplicando la que ya tenemos con **ctrl+d**, esta nueva caja la posicionaremos en:

- x = 4
- y = 0
- z = 12

![graficas](/graphics/assets/img/118_lab1.png)

Agregaremos otra caja y esta tendra su posición en:

- x = 6
- y = 0
- z = 12

![graficas](/graphics/assets/img/119_lab1.png)

Agregaremos una cuarta caja y la posicionaremos en:

- x = 3
- y = 1.6
- z = 12

![graficas](/graphics/assets/img/120_lab1.png)

Ahora vayamos por la quinta caja la cual estará en:

- x = 5
- y = 1.6
- z = 12

![graficas](/graphics/assets/img/121_lab1.png)

Vayamos por la última caja la cual estará en:

- x = 4
- y = 3.2
- z = 12

![graficas](/graphics/assets/img/122_lab1.png)

Con esto ya tenemos lista nuestra pirámide, si ejecutamos el proyecto y nos vamos de lleno contra está entonces las cajas saldrán volando por el impacto.

Ahora vamos a ver como cambiar las propiedades de un prefab nos permite modificar a un grupo de elementos prefab.

Modifica la masa del prefab a 100 y luego selecciona cualquiera de las cajas de la jerarquía, observa como de manera automática se actualiza el valor.

Esta es una de las importancias de los prefab, que otros comportamientos podemos extender, por ejemplo, podríamos programar con un script alguna de nuestras cajas, por ejemplo como items de recolección estilo Mario Bros donde las cajas estén rotando en su propio eje. Así solo el rotar sería un script para cualquier caja que agregemos, y ya la interacción entre caja y vehículo se haría con otro script que pudiera estar alineado directamente al vehículo.

El uso de los prefab ya nos da la oportunidad de extender enormemente la jugabilidad de nuestro proyecto.

Lo siguiente que haremos será crear un objeto vacío al cual llamaremos Piramide1.

![graficas](/graphics/assets/img/122_lab1.png)
![graficas](/graphics/assets/img/124_lab1.png)

Ahora arrastraremos nuestras 5 cajas al objeto **Piramide1**

![graficas](/graphics/assets/img/125_lab1.png)

Ahora haremos algo similar a lo que hicimos con el objeto de **Obstaculos**. Vamos a duplicar la Piramide1 y la vamos a colocar de manera arbitraria como se muestra a continuación.

![graficas](/graphics/assets/img/126_lab1.png)

Vamos a hacer este mismo proceso 4 veces más para tener un camino en zig zag con un total de 6 pirámides como se muestra.

![graficas](/graphics/assets/img/127_lab1.png)

Siguiendo la misma estructura de lo que hemos aprendido hasta el momento, crearemos un nuevo objeto vacío que se llame **Piramides** y arrastraremos todas nuestras piramides adentro para tenerlas agrupadas.

![graficas](/graphics/assets/img/128_lab1.png)

Para practicar vuelve a repetir el ejercicio creando 3 objetos originales así como lo hicimos con la pirámide, usa tu creatividad y los modelos que vienen de los otros obstáculos en el **Course Library>Obstacles**.

Recuerda no borrar tus piramides si te estorban, solo deshabilitarlas.

![graficas](/graphics/assets/img/129_lab1.png)

Una vez que tengas tus 3 objetos originales tomales un screenshot y añadelos a tu reporte, explica por que decidiste hacerlos así y tomar esos modelos.

### Paso 2 Autobús como prefab

Con lo que vamos a trabajar ahora es unir todo lo que hemos aprendido hasta el momento y obtener vehículos que vengan en sentido contrario para añadir un poco más de dificultad a nuestro juego.

Por ahora vamos a dejar limpia nuestra pista ocultando los obstaculos que no estamos utilizando.

Ahora vamos a añadir a nuestra escena desde **Course Library > Vechicles** el autobús azul.

![graficas](/graphics/assets/img/130_lab1.png)

Una vez hecho esto vamos a modificar la rotación del objeto en el eje y a -180, esto para que esté de frente a nuestra camioneta.

![graficas](/graphics/assets/img/131_lab1.png)

Ahora vamos a posicionar el autobús al final de nuestra carretera asignándole un valor de:

- x = -5
- y - 0
- z = 170

Ahora añadiremos al autobús el **rigibody** y vamos a asignarle una masa de 700.

![graficas](/graphics/assets/img/132_lab1.png)

Con esto ya está listo nuestro autobús, ahora solo lo arrastraremos a nuestra carpeta de **Prefabs**.

Por legibilidad vamos a renombrar nuestros  prefabs, el primero a Caja, y el que acabamos de crear a Autobus_azul.

![graficas](/graphics/assets/img/133_lab1.png)

Agregaremos a la escena otro autobus desde nuestro nuevo creado prefab y lo posicionaremos en:

- x = 5
- y = 0
- z = 150

![graficas](/graphics/assets/img/134_lab1.png)

### Paso 3 Script mover hacia adelante, obstáculos en movimiento

Para seguir evolucionando nuestro proyecto vamos a crear un script nuevo que se llame **MoveForward**.

Una vez creado iremos a nuestro editor y añadiremos la siguiente variable global.

```
public int speed;
```

Dentro de nuestro método **Update()** vamos a agregar un transform como en nuestro **PlayerController** que sería de la siguiente forma.

```
void Update()
{
    transform.Translate( Vector3.forward * speed * Time.deltaTime);
}
```
Ahora vamos a enlazar nuestro script con el prefab del autobús azúl, entonces teniendo seleccionado el prefab, vamos a arrastrar el script de **MoveForward**. De una vez vamos a cambiar la velocidad a un valor de 10.

![graficas](/graphics/assets/img/135_lab1.png)

Si ejecutamos el proyecto veremos como los 2 autobuses empezarán a venir hacia nosotros.

Como reto de práctica crea 6 autobuses más y así como los obstáculos y las pirámides crear un zig zag para que podamos jugar como se muestra a continuación.

Igualmente como los obstáculos anteriores crearemos un objeto vacío al cual llamaremos **Autobuses** y añadiremos nuestros 8 elementos creados.

### Paso 4 Cámara Principal y Secundaria

Un elemento muy común en los juegos actuales, es el poder cambiar entre diferentes modos de visualizacón de juego, por ejemplo primera persona a tercera persona.

Este efecto lo podemos tener muy facilmente usando el efecto de cámaras en nuestro proyecto.

Tomando nuestro script de **PlayerController** y añadiremos 3 variables globales.

```
//Variables cámara
public Camera mainCamera;
public Camera hoodCamera;
public KeyCode switchKey; //Tecla que permite cambiar entre cámaras
```

Dentro de nuestro método **Update()** añadiremos lo siguiente.

```
void Update()
{
    horizontalInput = Input.GetAxis("Horizontal");
    forwardInput = Input.GetAxis("Vertical");

    transform.Translate(Vector3.forward * Time.deltaTime * speed * forwardInput);
    transform.Rotate(Vector3.up, Time.deltaTime * turnSpeed * horizontalInput);

    //Cambio entre cámaras
    if(Input.GetKeyDown(switchKey))
    {
        mainCamera.enabled = !mainCamera.enabled;
        hoodCamera.enabled = !hoodCamera.enabled;
    }
}
```

Ya que tenemos nuestro código actualizado ahora vamos a hacer los ajustes en nuestro proyecto para poder ver la nueva funcionalidad.

En primer lugar estamos hablando de cambiar entre cámaras, sin embargo tenemos un pequeño problema, solo tenemos 1. Por lo tanto agregaremos una nueva cámara desde el menú donde agregamos nuevos objetos vacíos.

![graficas](/graphics/assets/img/136_lab1.png)

Ahora como vamos a trabajar con otra cámara, si intentamos poner ambas al mismo tiempo puede que Unity nos de errores, por lo tanto para este caso particular abriremos desde la jerarquía los componentes que conforman nuestro **Vehiculo**.

![graficas](/graphics/assets/img/137_lab1.png)

Lo que haremos será arrastrar nuestra nueva cámara al conjunto de parte que conforman **Vehiculo**.

![graficas](/graphics/assets/img/138_lab1.png)

Una vez hecho esto vamos a posicionar nuestra cámara de la siguiente forma.

- x = -0.2
- y = 1.95
- z = 0.26

Con estas coordenadas la cámara se ve desde el punto como si estuvieramos conduciendo.

![graficas](/graphics/assets/img/139_lab1.png)

Y ahora una vez posicionada la cámara vamos a deshabilitarla de inicio. **Ojo: Este punto es el más importante, si no lo haces no funcionará y te mandará errores**

![graficas](/graphics/assets/img/140_lab1.png)

Ya que tenemos configurada nuestra cámara, seleccionaremos nuevamente nuestro **Vehiculo** y nos iremos al **Inspector** a las opciones que definimos en nuestro script. Como ya hicimos en ejercicios anteriores asignaremos los objetos correspondientes a la **Main Camera** y a la **Hood Camera** así como asignaremos una tecla para hacer el cambio entre las mismas, para mí caso he seleccionado la tecla **C** para mantener la unicidad.

Nota que como la nueva cámara ya es parte de Vechiculo, toma en automático sus coordenadas a diferencia de la cámara principal que actua por su propia cuenta y por ello tuvimos que crear el script **FollowPlayer**

### Paso 5 Input ID

La última parte de este laboratorio se enfoca en la creación de un juego multiplayer local, esto requiere un poco más de conceptos avanzados, pero nada imposible de realizar.


Dentro de nuestra carpeta de scripts abriremos **PlayerController** y crearemos una nueva variable global.

```
//Variables multijugador
public string inputId;
```

Después dentro del método **Update()** vamos a modificar las declaraciones del horizontalInput y el forwardInput.

```
void Update()
{
    horizontalInput = Input.GetAxis("Horizontal" + inputId);
    forwardInput = Input.GetAxis("Vertical" + inputId);

    transform.Translate(Vector3.forward * Time.deltaTime * speed * forwardInput);
    transform.Rotate(Vector3.up, Time.deltaTime * turnSpeed * horizontalInput);

    //Cambio entre cámaras
    if(Input.GetKeyDown(switchKey))
    {
        mainCamera.enabled = !mainCamera.enabled;
        hoodCamera.enabled = !hoodCamera.enabled;
    }
}
```

Esto lo que nos va a permitir es determinar que jugador está utilizando el script de **PlayerController**.

### Paso 6 Configuraciones del Teclado

Si estamos hablando de un juego multiplayer local, entonces debemos entender que según como configuremos nuestra interacción al menos de forma muy simple podríamos configurar el teclado para ambos jugadores.

Si queremos realizar este comportamiento entonces necesitamos abrir los **project settings**.

![graficas](/graphics/assets/img/142_lab1.png)

Lo que vamos a hacer esduplicar la configuración Horizontal dando clic derecho sobre el Horizontal, seleccionando la opción **Duplicate Array Element**.

![graficas](/graphics/assets/img/143_lab1.png)

Ahora vamos a modificar los valores que trae nuestra nueva configuración a lo siguiente.

- Name: Horizontal1
- Negative Button: a
- Positive Button: d
- Alt Negative Button: {vacío}
- Alt Positive Button: {vacío}

![graficas](/graphics/assets/img/144_lab1.png)

Nuevamente duplicaremos nuestra opción pero ahora a partir de Horizontal1, quedando algo como esto.

![graficas](/graphics/assets/img/145_lab1.png)

Y los valores que agregaremos a esta nueva configuración serán.

- Name: Horizontal2
- Negative Button: left
- Positive Button: right
- Alt Negative Button: {vacío}
- Alt Positive Button: {vacío}

![graficas](/graphics/assets/img/146_lab1.png)

Ahora crearemos las configuraciones para Vertical quedando algo como.

- Name: Vertical1
- Negative Button: w
- Positive Button: s
- Alt Negative Button: {vacío}
- Alt Positive Button: {vacío}

![graficas](/graphics/assets/img/147_lab1.png)

Y creamos la segunda configuración.

- Name: Vertical2
- Negative Button: up
- Positive Button: down
- Alt Negative Button: {vacío}
- Alt Positive Button: {vacío}

![graficas](/graphics/assets/img/148_lab1.png)

Ahora si ejecutamos el proyecto como está podremos notar que a nivel de jugabilidad nada a cambiado, podemos seguir moviéndonos normalmente con el teclado.

Lo que debemos hacer ahora es eliminar las configuraciones default de Horizontal y Vertical ya que nos estarán haciendo sombra y no nos permitirán mover como esperamos.

![graficas](/graphics/assets/img/149_lab1.png)

El resultado final de mis configuraciones de entrada deben ser 4 perfiles que separan la jugabilidad por jugador.

### Paso 7 Jugador 2

Empecemos de lleno a esta parte, dentro de nuestra jerarquía seleccionemos nuestro **Vehiculo** y vamos a duplicarlo, además de que vamos a renombrarlo como **Player2**

![graficas](/graphics/assets/img/150_lab1.png)

De la misma manera vamos a duplicar nuesta **Main Camera** y la renombramos como **Player2Cam**.

![graficas](/graphics/assets/img/151_lab1.png)

Ahora vamos a seleccionar nuestra **Main Camera** y dentro del **Inspector** vamos a identificar el **Viewport Rect** y dentro de sus valores modificaremos w = 0.5.

![graficas](/graphics/assets/img/152_lab1.png)

Como resultado vemos que los ojos de cada cámara se expanden tal y como lo hacen los juego multiplayer locales en modo divided screen.

Ahora seleccionaremos la **Camera** que se encuentra dentro de **Vehiculo** e igualmente modificaremos el **Viewport Rect** en w = 0.5 para dar este mismo efecto en la cámara de primera persona.

Haremos esta misma modificación en el **Player2** pero además de cambiar el **Viewport Rect** en w = 0.5, vamos a modificar el valor en x -0.5.

El resultado es que se alinean las cámaras segun cada jugador, aunque por ahora están en la misma posición.

![graficas](/graphics/assets/img/153_lab1.png)

Para hacer el acomodo sencillo de nuestros jugadores vamos a acomodarlos arbitrariamente en un carril cada uno solo moviendolos a través del eje x dando un resultado como el siguiente.

![graficas](/graphics/assets/img/154_lab1.png)

Ahora las cámaras de cada jugador aún no están siguiendo a su correspondiente, de momento esto está bien y la visualización que tenemos en el game view es correcto. Pero si ejecutamos el proyecto veremos que aunque la cámara se posiciona detrás del jugador, la **Player2Cam** no se va con **Player2** sino con **Vehiculo**.

De momento está bien, solo para asegurarnos que todo está en orden, **Vehiculo** colocalo en x = -5 y **Player2** en x = 5.

### Paso 8 Cámara Player2

Para corregir el detalle de la cámara en  **Player2** vamos a seleccionarlo y nos vamos a la propiedad del script de **PlayerController** y la **Main Camera** vamos a modificarla por la **Player2Cam**.

![graficas](/graphics/assets/img/155_lab1.png)

Por último vamos a seleccionar la **Player2Cam** y en la propiedad del script de **FollowPlayer** vamos a modificar el Player por el **Player2**.

![graficas](/graphics/assets/img/156_lab1.png)

Si ejecutamos nuevamente veremos como ahora sí, se posicionan las cámaras en sus respectivos lugares con los jugadores.

Y como observación adicional, presiona la tecla c para cambiar entres las cámaras y automáticamente la cámara de ambos vehículos se acomodará en su respectivo.

Para evitar el salto inicial y para tener nuestra **Main Camera** y nuestra **Player2Cam** en su lugar desde el inicio vamos a modificar sus pocisiones en x para -5 y 5 según sea el caso.

### Paso 9 Cámara  1era Persona

Por el momento si presionamos la tecla **c** cambia el modo de cámara de ambos jugadores, entonces vamos a modificar la tecla, y vamos a asignarle el **right shift**.

![graficas](/graphics/assets/img/157_lab1.png)

Si ejecutamos y presionamos **c** ó **right shift** veremos el resultado para cada jugador.

> Si aún tienes la duda de por que modificamos **Player2Cam** y no el **Camera** de nuestro **Player2**, esto es por que las **Camera** pertenecen directamente a los elementos del **Vehiculo** y a **Player2** por lo que en este caso se ajusta directamente.

### Paso 10 Funcionalidad Player2

Ya podemos mover cada cámara de forma independiente, pero aún no podemos mover ninguno de los vehículos.

Dentro del **Player2** en el **Inspector** en los parámetros del **PlayerController** vamos a asignar el **InputId** con un valor de 2.

![graficas](/graphics/assets/img/158_lab1.png)

Como ejercicio ahora deberás lograr que se mueva el **Vehiculo** o el Player 1.

### Paso 11 Funcionalidad Player1

Si lo lograste y como intuiste para mover el jugador 1 solo hace falta con asignar el **InputId** de **Vehiculo** a un valor de 1.

![graficas](/graphics/assets/img/159_lab1.png)

Si te preguntas por que solo es necesario agregar el 1 y el 2 para dar la funcionalidad a ambos jugadores, la explicación es muy simple, recuerda que cuando creamos las configuraciones en el Input Manager, creamos la configuración de

Horizontal1 y Vertical1
Horizontal2 y Vertical2

Si extraemos una de las líneas de código del **PlayerController** veremos lo siguiente.

```
horizontalInput = Input.GetAxis("Horizontal" + inputId);
```

Lo que recibe **Input.GetAxis()** es un String con el nombre de la configuración que necesitamos llamar, y en este caso solo necesitamos añadir el 1 o el 2 que es justamente el parámetro de la variable InputId.

Esto nos permite que cada objeto en la escena tenga su propio valor y unificar los valores dentro de 1 solo script.

Bien podríamos haber duplicado el código para hacer esto, pero en términos de mantenibilidad y buenas prácticas debemos evitar el código duplicado lo más posible tanto a nivel de funciones como a nivel de ejecución.

Si seguiste la práctica hasta ahora habrás notado que todo funciona bien, excepto que al presionar arriba o abajo de ambos jugadores, están invertidos los valores.

Como ejercicio adicional, corrige estos para que funcionen correctamente.

El último requisito del laboratorio es que con todo lo aprendido y con lo que ya tenemos realizado, hagas un pequeño nivel usando los prefabs de obstáculo y otras mecánicas que se te ocurran para finalizar el proyecto.

Deberás crear un video de no más de 30 segundos donde muestres tu resultado final, y deberás añadirlo a tu reporte, de preferencia subelo aparte en otro lado como youtube para solo acceder a verlo.