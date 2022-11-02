# Físicas y Obstáculos en Unity

## Objetivo
En este laboratorio extenderemos la funcionalidad del laboratorio anterior añadiendo más control e interacción para tener un vehículo más creíble en cuestión de la realidad.

## Instrucciones
Sigue los pasos descritos en la siguiente práctica, si tienes algún problema no olvides que tus profesores están para apoyarte.

## Laboratorio
### Paso 1 Modificando la velocidad

En la última parte nos quedamos agregando la primera línea de código del vehículo, sin embargo si recuerdas al ejecutar el código, la camioneta toma toda la velocidad y sale volando del espacio visible. Este comportamiento no es el adecuado o el que esperamos que tenga un juego normal, puesto que tratamos de emular un vehículo, esperamos que al menos se detenga con el límite del mundo o al menos no parezca un objeto que no pertenece a este mundo.

Para ello debemos empezar a involucrar uno de los elementos más importantes en la realidad para el ser humano, la física, añadiendo las formulas básicas podemos mejorar en gran medida el comportamiento del vehículo para hacerlo más creíble.

Para comenzar, abre el script de **PlayerController** y desde donde nos quedamos comenzaremos con esta nueva línea de código.

```
Time.deltaTime
```

Esta clase y función será muy útil para nosotros, pues para lo que nos sirve es que es el intervalo de tiempo que hay entre cada uno de los fotogramas, esto quiere decir para la función Update cada cuanto tiempo se está llamando, algo importante a notar es que este intervalo es muy pequeño e incluso se mide en milisegundos. Lo que haremos con este intervalo es el "realentizar" y esto es solo a nivel visual puesto a que realmente no se está modificando, en otro término sería ajustar la velocidad al tiempo el cual está corriendo nuestro juego.

Entonces, para involucrar el tiempo al código que ya tenemos lo único que debemos hacer es lo siguiente.

```
void Update()
{
    //Mover vehiculo hacia adelante
    //transform.Translate(0,0,1);
    transform.Translate(Vector3.forward * Time.deltaTime);
}
```

Si ejecutamos el proyecto nos daremos cuenta que si hay un cambio significativo, ahora la camioneta va demasiado lento. Ahora lo que resta es jugar un poco con los valores para saber que tando queremos aumentar la velocidad, y esto nos permitar parametrizar la velocidad o incluso si somos creativos crear toda una caja de velocidades para nuestro vehículo.

Para nuestro caso multiplica por un valor de 5 unidades y vuelve a correr para empezar a ver una diferencia.

```
void Update()
{
    //Mover vehiculo hacia adelante
    //transform.Translate(0,0,1);
    transform.Translate(Vector3.forward * Time.deltaTime * 5);
}
```

Si queremos tomar un cierto estándar podemos decir que sería un valor de 20, entonces vamos a actualizarlo y observa que el movimiento se ve un poco más creíble a lo que pudieramos esperar de un videojuego.

```
void Update()
{
    //Mover vehiculo hacia adelante
    //transform.Translate(0,0,1);
    transform.Translate(Vector3.forward * Time.deltaTime * 20);
}
```

### Paso 2 Agregando Física

Ta que tenemos una velocidad "normal" para nuestro vehículo ahora agregaremos la física para nuestro vehículo como de nuestro obstáculo.

El problema actual es que al avanzar el vehículo pasa sobre nuestra caja como si nada.

Para comenzar seleccionaremos nuestro vehículo.

![graficas](/graphics/assets/img/76_lab1.png)

Ahora vamos a añadir un componente desde nuestro **Inspector**, recuerda que el botón **Add Component** se encuentra hasta abajo de las propiedades que contienen nuestro objeto en este caso el vehículo.

Ahora dentro de las opciones de componentes que tenemos para añadir a nuestro objeto vamos a buscar la que se llama **Rigidbody**

![graficas](/graphics/assets/img/77_lab1.png)

Vamos a repetir este mismo proceso con el obstáculo, y en ambos objetos verás que en el inspector se agrega el componente como se muestra para el caso del obstáculo.

![graficas](/graphics/assets/img/78_lab1.png)

Si volvemos a ejecutar vamos a ver un cambio bastante drástico en lo que teniamos inicialmente.

![graficas](/graphics/assets/img/79_lab1.png)

Finalmente nuestra vehículo impacta con el obstáculo. Pero no solo eso, cuando la camioneta llega al final del camino simplemente cae al vacío.

Ahora, vamos a hacer un poco más "real" estas interacciones con los objetos, modificando el peso de los mismos.

Si revisamos en el inspectos las propiedades del rigidbody nos daremos cuenta de la propiedad de **mass** o masa del objeto.

![graficas](/graphics/assets/img/80_lab1.png)

Te invito a que experimentes con diferentes valores para ambos objetos (vehículo y obstáculo) y ve que diferencias hace el que uno sea más que otro y el uso de valores bajos y altos.

Para dejar el mismo valor de nuestro lado yo estaré dejando un valor de **1000 al vehículo** y de **50 al obstáculo**

Ahora para poder analizar el siguiente elemento, voy a reducir la velocidad del vehículo a 10.

```
transform.Translate(Vector3.forward * Time.deltaTime * 10);
```

Lo que vamos a hacer es correr el vehículo y justo antes de impactar la caja vamos a **pausar** la ejecución.

El resultado debe ser algo como lo siguiente.

![graficas](/graphics/assets/img/81_lab1.png)

Como puedes ver, técnicamente la caja y la camioneta no estan colisionando del todo, sino que al tener resaltado como esta consturido el vehículo vemos que tiene un pequeño triángulo de frente que sirve como colisionador y que al tocar la caja la empieza a mover.

Por su parte su yo verifico como se constriuye la caja veremos que en este caso no cuenta con adicionales, sino que toda su construcción es el cubo que representa.

![graficas](/graphics/assets/img/82_lab1.png)

Las líneas verdes son el collider o colisionador, todo lo que choca con estas lineas o en ese rango van a tener una física, si lo quitamos, el cuerpo está ahí, pero pasaría como al inicio, atravesariamos los objetos.

Los objetos más detallados de los videojuegos tienen polígonos de colisión muy detallados para dar un mejor efecto y evitar lo que sucede con el carro que realmente nunca toca la caja al menos de frente.

Como experimento vamos a quitar el colisionador de la caja y vamos a ejecutar.

![graficas](/graphics/assets/img/83_lab1.png)

Si ejecutamos el nuevamente veremos como la caja cae atravesando la carretera. Esto sucede por que al tener un **rigidbody** nuestro objeto tiene física, pero al no tener un **collider** simplemente se va a ir hacia abajo.

![graficas](/graphics/assets/img/84_lab1.png)

Se regresamos el collider, ahora sí se ajusta al suelo de la carretera como lo teniamos inicialmente.

### Paso 3 Agregando Obstáculos

Con lo que hemos hecho hasta ahora, si te pido agregar más obstáculos, ¿Cómo lo harías?

Si tu respuesta es a través del course library > vehicles y seleccionamos la caja, es correcto.

Sin embargo, habrá ocasiones que necesitamos hacer copias de objetos de manera más eficiente, ya que de la forma actual tenemos que estar navegando y buscando elementos e incluso podemos equivocarnos agregando algo que no queremos en ese momento.

Otro de los problemas que tenemos al cargar desde "0" nuestro objeto, es que para el caso de la caja, nosotros agregamos un **rigidbody** al objeto que ya tenemos, entonces los objetos del course library no cuentan con este componente, por lo que tendríamos que generar para cada objeto nuevo un **rigidbody** propio lo cual extendería demasiado el tiempo de trabajo y se haría tedioso. 

Para hacer las cosas más fáciles podemos duplicar objetos ya existentes desde nuestra jerarquía utilizando el comando **ctrl+d**. Al ser el duplicado ya tenen para el caso del obstáculo una **rigidbody** e incluso la misma propiedad de masa que habíamos colocado de 50.

Incluso si quisiera hacer una producción en masa, puedo seleccionar los 2 obstáculos que ya cree, usando la tecla **shift** y al tener ambor nuevamente usar el comando **ctrl+d** con esto veremos que se duplican los 2 que ya tenía dando un resultado de 4 o 6 según los que hayas duplicado inicialmente.

![graficas](/graphics/assets/img/85_lab1.png)

Vamos a borrar todos los duplicados creados dejando solo el original.

Ahora lo que vamos a hacer es tener 3 cajas para hacer de obstáculos para el vehículo por lo que primero duplicaremos la caja 2 veces.

![graficas](/graphics/assets/img/86_lab1.png)

Ahora para cada caja vamos a modificar su coordenada z empezando con la primera en la pocisión 25, y después añadiremos +15 a cada una de las siguientes. El resultado deberá verse como se muestra.

![graficas](/graphics/assets/img/87_lab1.png)

Si mantengo seleccionadas las 3 cajas voy a ver que tengo la posibilidad de mover con las flechas de los ejes x,y,z las mismas.

Si yo muevo con las flechas del eje z, puedo ver que al tener las 3 seleccionadas se mueven todas a pesar de que solo me aparezcan las flechas del último objeto seleccionado.

![graficas](/graphics/assets/img/88_lab1.png)

Si yo duplicara nuevamente la selección puedo mover a tener 6 cajas perfectamente alineadas dandome mayor facilidad de crear obstáculos para mi vehículo.

Para comenzar me quedaré solo con 3 cajas, pero modificaré la distancia entre ellas para que sea más fácil maniobrar. 

- La primera quedará en z=25
- La segunda en z = 75
- La tercera en z = 120

![graficas](/graphics/assets/img/89_lab1.png)

Ahora duplicaré esas 3 cajas y las movere de manera arbitraria a más o menos 1/4 de la distancia de la siguiente caja. Además de moverlas un poco a la izquiera en el eje x.

![graficas](/graphics/assets/img/90_lab1.png)

Finalmente duplicaré nuevamente las cajas y las moveré otro cuarto de distancia arbitrari y ahora las jalaré hacia la derecha dandome el siguiente resultado.

![graficas](/graphics/assets/img/91_lab1.png)

Si ejecutamos el juego, ve el resultado que aunque no hay interacción, al tener de frente las 3 cajas observa lo que sucede.

Esta es una forma muy básica de agregar obstáculos, obviamente no es la forma más optimizada de hacerlo pero nos da algunas nociones adicionales para el trabajo con mayor cantidad de objetos.

Intenta jugar nuevamente con la masa del vehículo y ve como se afecta al interactuar con varios objetos en su camino, y que tanto puede llegar a afectar su comportamiento.

Para resultados finales deja la masa del vehículo con un valor de **500**.

### Paso 4 Modificar la velocidad desde el inspector

Ahora que ya tenemos más objetos y podemos jugar con la masa de cada uno, veremos que la velocidad tenemos que estarla cambiando manualmente en nuestro script de **PlayerController**, si bien podemos estar acostumbrados a esto por la dinámica de programación, sería más fácil poder hacerlo directamente desde Unity, veremos como hacerlo posible en este paso.

Dentro de nuestro script vamos a agregar una variable global para el manejo de la velocidad.

```
public float speed = 5.0f;
```
El resultado final sería el siguiente, checa que añadimos la variable a la función de transform.

```
public class PlayerController : MonoBehaviour
{
    //velocidad del vehículo
    public float speed = 5.0f;
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        //Mover vehiculo hacia adelante
        //transform.Translate(0,0,1);
        transform.Translate(Vector3.forward * Time.deltaTime * speed);
    }
}

```

Si ejecutamos nuevamente veremos que ahora la velocidad es menor. Sin embargo, si nos vamos al **Inspector** y luego a nuestro componente del script observaremos que se añadió la velocidad como parámetro.

![graficas](/graphics/assets/img/92_lab1.png)

Y no solo eso, además de poder establecer un valor inicial, podemos ir modificando la velocidad conforme se ejecuta nuestro juego y se verá como acelera la camioneta según el valor que le demos.

Como valor final en el parámetro del **Inspector** la vamos a dejar en 25.

**Nota:Si estás en modo play, y modificas el valor de la velocidad, al detenerse regresará al valor que tenía originalmente, y en caso de no haberlo modificado tomará el valor default que tiene el script de 5.**

### Paso 5 Script FollowPlayer

Ya que tenemos dominada la física y la velocidad, ahora vamos a hacer uno de los puntos más importantes de un buen juego y que al menos hasta ahora en nuestra vista de juego no hemos modificado, la cámara.

Si bien ya teniamos posicionada la cámara, hasta este punto es estática.

Lo que vamos a realizar es que nuestra cámara siga a nuestro vehículo como un juego en 3era persona.

Para hacer esto vamos a crear un nuevo script que se llame **FollowPlayer**

![graficas](/graphics/assets/img/93_lab1.png)

Ahora añadiremos el script a la cámara que en este caso será el elemento que queremos utilizar.

![graficas](/graphics/assets/img/94_lab1.png)

Una vez que tenemos esto abriremos el código en nuestro editor o IDE, nuevamente veremos que tenemos el código que se genera de manera automática y que aplica para todos los objetos de nuestra escena.

Lo primero que haremos es crear una variable global de esta manera.

```
public GameObject player;
```

Una vez hecho esto se añadira una propiedad en el **Inspector** para agrar un objeto de la escena, este paso es el más importante.

![graficas](/graphics/assets/img/95_lab1.png)

Una vez que nos aparezca, vamos a tomar de la jerarquía nuestro Vehículo y lo vamos a arrastrar al espacio del Player, o en sud efecto si seleccionas el punto que viene del parámetro te dejara buscar el objeto, cualquiera de las 2 opciones es válida.

El resultado debe verse como lo que sigue.

![graficas](/graphics/assets/img/96_lab1.png)

Ya que tenemos conectado nuestro objecto vehículo como componente de la cámara, ahora seguiremos con nuestro script.

En el método Update vamos a agregar lo siguiente:

```
void Update()
{
    transform.position = player.transform.position;
}
```

En pocas palabras estamos haciendo que la cámara tome la pocisión de nuestro vehículo. Como resultado que aparentemente lo siga.

Si lo ejecutamos vamos a ver un detalle, todo se ve en verde hasta que vemos caer el vehículo encima de nosotros.

Esto sucede por que al darle la misma posición de coordenadas de la cámara que el vehículo, la cámara pierde la altura que ya teniamos acomodada.

### Paso 6 Agregar offset a la cámara

Para solucionar el problema de la cámara necesitamos repocisionarla con la altura que necesitamos.

Para hacerlo dentro de nuestro script solo necesitamos agregar lo siguiente.

En la línea de asignación de la posición que teniamos vamos a agregar lo siguiente.

```
transform.position = player.transform.position + new Vector3(0,6,-7);
```

Te preguntarás por que estas coordenadas, y esto es por que son las coordenadas con las que inicialmente tenemos posicionada la cámara y que al menos nosotros sabemos son la forma que nos interesa ver la camioneta.

![graficas](/graphics/assets/img/97_lab1.png)

Si ejecutamos nuevamente, veremos que ahora si la cámara sigue efectivamente nuestro vehículo, incluso aumenta la velocidad y observa como esto no afecta.

Ahora para limpiar un poco el código vamos a crear una variable global privada que tome los valores de offset.

```
private Vector3 offset = new Vector(0,6,-7);
```

El resultado de nuestro **FolloPlayer** sería entonces.

```
public class FollowPlayer : MonoBehaviour
{
    public GameObject player;
    private Vector3 offset = new Vector3(0,6,-7);

    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        transform.position = player.transform.position + offset;
    }
}

```

Si ejecutamos nuevamente veremos que todo sigue funcionando correctamente.

### Paso 7 Método LateUpdate

Algo que se nota al momento de ejecutar el juego, al inicio hay como que un pequeño salto o vibración rara de parte del carro. Para un usuario final quizás no es tan perceptible, pero para nosotros como desarrolladores al estar ejecutando el juego constantemente se empieza a hacer molesto.

Para arreglar esto nos iremos al script de **FollowPlayer**, ahora veremos un nuevo método del ciclo de vida del juego, este método es conocido como **LateUpdate()** es similar a **Update()** en que se llama todo el tiempo, la diferencia y como puedes estar sospechando es que se manda llama inmediatamente después del método **Update()**. Esto nos permite que una vez que se ejecuta todo el juego, se puede cargar las cosas de una manera más "suave" ya que no se hará todo el cambio de la cámara tan abrupto que es lo que sucede actualmente.

Entonces en **FollowPlayer** vamos acambiar la declaración de **Update** por **LateUpdate()**.

Nuevamente ejecutamos y podremos ver que el inicio será más "suave" o más normal, si aún no te percatas de que es lo que sucede vuelve a regresar al método **Update()** e intercala hasta que logres ver la diferencia, es sútil pero está ahí.

> Recuerda que lo más importante en estos temas de gráficas, son los detalles. Si bien es fácil hacer las cosas, son los detalles los que hacen la diferencia entre un buen y un mal (juego,película, efecto, simulación...etc.)

### Paso 8 Modificar PlayMode

Si bien en pasos anteriores habíamos modificado nuestro layout en Unity para tener más facilmente el acomodo y poder trabajar de una mejor forma.

Recurdas que te mencionaba que al ejecutar el juego pasamos como a un segundo plano, donde se hace más oscuro el editor, y si bien podemos modificar los parámetros como el de la velocidad, al detener el juego y regresar al modo normal, los valores igualmente regresan a su estatus inicial.

En ocasiones por el default de Unity no nos damos cuenta si estamos en modo juego o en modo edición.

Es por ello que yo modifiqué el color al momento de ejecutar a lo que te muestro a continuación.

![graficas](/graphics/assets/img/98_lab1.png)

Si ves el color que escogí para mi editor es ese azul verdoso, y ahora es momento que modifiques el tuyo.

Para hacer esto nos iremos a **edit > Preferences...**

![graficas](/graphics/assets/img/99_lab1.png)

Después en el panel que nos abre seleccionaremos la opción de **colors**.

![graficas](/graphics/assets/img/100_lab1.png)

Y ahora buscaremos  el **playmode tint**

![graficas](/graphics/assets/img/101_lab1.png)

Ahora selecciona el color y busca uno que se adecue a tus preferencias, solo que **ojo: verifica que tenga un alpha o transparencia, ya que si deja el color base puede pintarte todo y ya no vas a distinguir entre los botones de play y pausa.**

También como puedes ver en este espacio de colores puedes modificar otros elementos del editor, si quieres ajusta lo que necesites de una vez, yo te recomiendo que mientras sigues aprendiendo lo dejes lo más default posible para evitar perderte, pero eso lo dejo a tu consideración.

### Paso 9 Mover vehículo de Izquierda a Derecha
Vamos a empezar con la interactividad de nuestro vehículo a partir del teclado.

Pero antes de ello necesitamos darle a nuestro vehículo la capacidad de girar.

Dentro de nuestro script de **PlayerController** vamos a crear una variable global que sea para la velocidad de giro de la siguiente forma.

```
public float turnSpeed = 0.0f;
```
![graficas](/graphics/assets/img/102_lab1.png)

Ahora siguiendo en nuestro script, en el método **Update()** vamos amodificar el giro.

```
void Update()
{
    //Mover vehiculo hacia adelante
    //transform.Translate(0,0,1);
    transform.Translate(Vector3.forward * Time.deltaTime * speed);
    //Modificar el giro
    transform.Translate(Vector3.right * Time.deltaTime* turnSpeed);
}
```

Con esto permitimos que nuestro vehículo vaya hacia la derecha, no olvidemos multiplicar por el deltaTime para ajustar a la velocidad de refrescado de los frames del juego.

Si ejecutamos el juego ajustando la velocidad en 5, y verificamos nuestro turnSpeed en el **Inspector** y empezamos a sumar o restar valores se ve como se va moviendo el vehículo a la izquierda o la derecha.

![graficas](/graphics/assets/img/103_lab1.png)

### Paso 10 Mover vehículo con teclado

Para poder interactuar con el teclado, necesitamos conocer como Unity nos ofrece las formas de interactividad para distintos periféricos, entre ellos el teclado.

Para comenzar vamos a irnor al menú de **edit> project settings**

![graficas](/graphics/assets/img/104_lab1.png)

Del panel que nos abre seleccinaremos la opción **input manager**.

![graficas](/graphics/assets/img/105_lab1.png)

Si desplegamos los **axes** veremos todas las posibles opciones de interactividad que tenemos. Esto al menos por defecto y que podemos utilizar ya. Lo que haremos será un input horizontal para hacer el movimiento de izquiera a derecha, el vertical sería para subir o bajar.

Si extendemos el **Horizontal** podemos observar los distintos parámetros que tenemos disponibles para configurar.

![graficas](/graphics/assets/img/106_lab1.png)

Ahora bien, ¿esto por qué nos interesa?, por que en el parámetro **Negative Button** dice **left** y en **Positive Button** dice **right** esto significa que la flecha izquierda nos va a decrementar valores mientras que la derecha nos sumara valores, también tenemos **Alt negative Button** y **Alt positive Button** que son la tecla **a** y **d** que son las teclas alternas que también podemos usar para el mismo fin.

Los demás valores te recomiendo dejarlos como están ya que son las configuraciones estándar para un juego, a menos que tengas un requerimiento particular entonces si deberías modificarlas.

Ahora para agregar la interacción con el teclado abriremos nuestro **PlayerController** y agregaremos la siguiente variable global.

```
public float horizontalInput;
```

Dentro del método **Update()** haremos lo siguiente.

```
void Update()
{
    horizontalInput = Input.GetAxis("Horizontal");

    //Mover vehiculo hacia adelante
    //transform.Translate(0,0,1);
    transform.Translate(Vector3.forward * Time.deltaTime * speed);
    //Modificar el giro
    transform.Translate(Vector3.right * Time.deltaTime* turnSpeed * horizontalInput);
}
```

Como puedes ver asignamos el **horizontalInput** y ¿por qué usamos el String de **Horizontal?**, no olvides que así es como se llama en el **InputManager**, entonces si quisieramos usar alguno de los otro Axis, solo bastaría con llamar a su correspondiente.

![graficas](/graphics/assets/img/107_lab1.png)

También observa que en el código se agrega a nuestro transform se agrega la multiplicación del **horizontalInput**.

Si ejecutamos el proyecto, y bajamos a las opciones de parámetros de nuestro script podemos observar el Horizontal Input y si presionamos la flecha de izquierda o derecha vemos como ganan valor hasta llega a -1 o 1 respectivamente.

Si intentamos modificar el **turnspeed** notaremos también que ahora no cambia la dirección de derecha a izquierda.

Esto sucede a que en la multiplicación de valores del transform, como inicialmente **horizontalInput** es 0 pues aunque exista la velocidad de giro todo se convertirá a 0.

Pero si le dejamos una velocidad de giro y apretamos las teclas veremos que si que se empieza a patinar de derecha a izquierda el vehículo.

Experimenta con los valores para que te quede claro el proceso.

Para el resultado final dejaremos los valores en:

- Velocidad = 20
- Velocidad de Giro = 20

Hasta este punto ya tenemos un juego donde la cámara sigue a nuestro jugador principal y que podemos mover de acuerdo a las teclas que presionemos, izquierda o derecha.

### Paso 11 Mover vehículo hacia adelante

Vamos a comenzar este paso con nuestro script de **PlayerController** añadiendo una nueva variable global.

```
public float forwardInput;
```

Y dentro del método **Update()** modificaremos el código añadiendo el input del Axis Vertical y en el transform del movimiento el forwardInput.

```
void Update()
{
    horizontalInput = Input.GetAxis("Horizontal");
    forwardInput = Input.GetAxis("Vertical");

    //Mover vehiculo hacia adelante
    //transform.Translate(0,0,1);
    transform.Translate(Vector3.forward * Time.deltaTime * speed * forwardInput);
    //Modificar el giro
    transform.Translate(Vector3.right * Time.deltaTime * turnSpeed * horizontalInput);
}
```

Vamos a ejecutar el proyecto y veamos que sucede.

De entrada el vehículo no se mueve hasta que presionamos la tecla arriba o abajo. Pero vamos a notar que si presionamos izquierda o derecha algo raro pasa, la funcionalidad sigue siendo correcta, pero naturalmente el vehículo no debería moverse así.

### Paso 12 Girar vehículo con rotate

Para modificar el comporamiento de nuestro vehículo lo que buscamos es que en vez de moverse de un lado a otro lo normal sería que gire, por lo tanto, dentro de **PlayerController** vamos a comentar el translate del giro y vamos a añadir.

```
transform.Rotate(Vector3.up,horizontalInput);
```

Con este nuevo método de rotate veremos que el Vector3 que utilizamos ya no es hacia la derecha puesto que ya no nos estamos desplazando, ahora giramos en sentido del eje z que en este caso es hacia arriba.

Añadiendo el horizontalInput agregamos el valor en grado que queremos que rote nuestra camioneta.

Si ejecutamos el proyecto podemo ver este cambio.

![graficas](/graphics/assets/img/108_lab1.png)

Este comportamiento es más normal a lo que podríamos esperar del vehículo.

Si nos ponemos estrictos, todavía hay muchos errores que podemos tener manejando el vehículo en el juego.

**Para tu reporte añade una lista de todos los posibles errores que identifiques en el juego.**

Por último vamos a terminar añadiendo la velocidad de giro y el Time.deltaTime para que se vea más ajustado a nuestro parámetros originales.

```
transform.Rotate(Vector3.up, Time.deltaTime * turnSpeed * horizontalInput);
```

Ya que tenemos nuestros valores como debería. Ahora vuelve a experimentar con los valores de velocidad de giro y termina de entender lo que está pasando.

Por último los valores que dejaremos en el vehículo son:
- Velocidad = 20
- Velocidad de giro = 45

### Paso 13 Arreglando detalles

Vamos a implementar buenas prácticas en nuestro código ordenandolo.

Es importante que el código este documentado para que alguien más pueda introducir cambios, el estándar lo puedes encontrar aquí. [C# Documentation](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/language-specification/documentation-comments)

En el **PlayerController** lo vamos a dejar de la siguiente manera.

```
/// <summary>
/// This player controller class will update the events from the vehicle player.
/// Standar coding documentarion can be found in 
/// https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/language-specification/documentation-comments
/// </summary>
public class PlayerController : MonoBehaviour
{
    public float speed = 5.0f;
    public float turnSpeed = 0.0f;
    public float horizontalInput;
    public float forwardInput;

    /// <summary>
    /// This method is called before the first frame update
    /// </summary>
    void Start()
    {
        
    }
    /// <summary>
    /// This method is called once per frame
    /// </summary>
    void Update()
    {
        horizontalInput = Input.GetAxis("Horizontal");
        forwardInput = Input.GetAxis("Vertical");

        transform.Translate(Vector3.forward * Time.deltaTime * speed * forwardInput);
        transform.Rotate(Vector3.up, Time.deltaTime * turnSpeed * horizontalInput);
    }
}
```

Como ejercio, comenta el código de **FollowPlayer** y anexalo a tu reporte.

Ya que tenemos ordenado nuestro código, ahora procederemos a ordenar nuestra jerarquía de juego. Dando clic derecho vamos a crear un objeto vacío y de nombre le pondremos **Obstaculos**.

![graficas](/graphics/assets/img/109_lab1.png)

Después vamos a seleccionar todos nuestros obstáculos, y vamos a arrastrarlos a este nuevo objeto vacío que acabamos de crear.

![graficas](/graphics/assets/img/110_lab1.png)

Con este nuevo objeto, ya no necesito seleccionar todos los objetos obstáculo para moverlos, con seleccionar al padre, ya puedo tomarlos todos como parte de un grupo.

De momento es todo por la sesión revisa, lo que debes de tener para tu reporte hasta el momento, el día de mañana finalizaremos con este laboratorio básico y la funcionalidad final del juego.