# Llamadas API en Unity

## Objetivo
En este laboratorio exploraremos el manejo de tiempo en Unity, utilizaremos la librería del sistema para ello y como objetivo podremos tener u proyecto que ejecute tiempo acelerado.

La aplicación a crear toma un rango de referencia de medio segundo en tiempo real para convertirlo en 1 min dentro de la simulación.

Igualmente el objetivo es que en cierto tiempo de la simulación se ejecute una acción dentro del proyecto.

## Instrucciones
Sigue los pasos descritos en la siguiente práctica, si tienes algún problema no olvides que tus profesores están para apoyarte.

## Laboratorio
### Paso 1 Crear un nuevo proyecto

Crea un nuevo proyecto en 2D y añade un TextMeshPro, como esta configuración es parte de lo que hemos trabajado en el laboratorio pasado prueba el conocimiento adquirido hasta el momento, si tienes dudas regresa al laboratorio anterior para hacer la configuración.

### Paso 2 Creando un cuadrado en 2D

Si bien por lo general ya tenemos assets que podemos utilizar de la tienda de Unity, quizás en ocasiones necesitemos trabajar con algunas formas primitivas como triángulos o polígonos en 2D, o figuras volumétricas como esferas, cuadrados, entre otros.

Para nuestro caso vamos a agregar un cuadrado, y lo haremos de la misma forma en la que agregamos el TextMeshPro.

Dando clic dereco en la jerarquía iremos a **2D Figures>Sprites>Rectangle**

![graficas](/graphics/assets/img/lab3/1_lab3.png)

A este le daremos una dimensión de escala de 100x100, y lo colocaremos en un extremo de la pantalla fuera de la vista de la cámara.

De momento no lo usaremos pero eventualmente usaremos el tiempo para que en determinado momento pase cruzando la cámara con un evento disparado. Trata de morificar el color del cuadrado a otro que no sea blanco para darle más personalidad a tu proyecto.

![graficas](/graphics/assets/img/lab3/2_lab3.png)

Ya que tenemos nuestra configuración básica empecemos con los scripts.

### Paso 3 TimeManager

Como siempre vamos a crear nuestra carpeta de **Scripts** dentro de la carpeta de **Assets** y hoy crearemos un script que tomará por nombre **TimeManager**.

![graficas](/graphics/assets/img/lab3/3_lab3.png)

Para esta clase agregamos como import a los que ya vienen por default la de sistema para poder trabajar con las funciones generales del sistema.

```
using System;
```

Como parte de las variables globales de nuestro script vamos a definir las siguientes

```
public static Action OnMinuteChanged;
public static Action OnHourChanged;

public static int Minute{get; private set;}
public static int Hour{get;private set;}

private float minuteToRealTime = 0.5f;
private float timer;
```

Las varibales **OnMinuteChanged** y **OnHourChanged** son de tipo **Action**, estas nos permitirán lanzar eventos a nuestro juego cuando nosotros indiquemos, y del lado de otros objetos recibirlos.

Notarás una sintáxis diferente para la definición de **Minute** y **Hour**, esto lo hacemos para definir la forma en la que podemos asignar y obtener los valores de las variables, indicando que cualquier elemento externo puede acceder a los valores, pero solo dentro del **TimeManager** se pueden modificar. Está sintáxis es propia de C# aunque en otros lenguajes también se utiliza esta misma notación.

Por último la variable **minuteToRealTime** no establece el intervalo de tiempo entre cuantos minutos en el juego equivalen a tiempo real, como definimos al inicio del laboratorio será de medio segundo en tiempo real para que pase 1 minuto en el juego.

La variable **timer** nos ayudará a saber el intervalo de tiempo antes de actualizar los valores.

Ahora dentro del método **Start()** agregaremos lo siguiente.

```
void Start()
{
    Minute = 0;
    Hour = 10;
    timer = minuteToRealTime;
}
```

Esto para inicializar nuestras variables al momento de iniciar el juego.

Ahora dentro del método **Update()** vamos a tener lo siguiente.

```
void Update()
{
    timer -= Time.deltaTime;

    if(timer <= 0)
    {
        Minute++;

        OnMinuteChanged?.Invoke();

        if(Minute >= 60)
        {
            Hour++;
            OnHourChanged?.Invoke();
            Minute = 0;
        }

        timer = minuteToRealTime;
    }
}
```

Vamos a inspeccionar el código, dentro de la primera línea tenemos

```
    timer -= Time.deltaTime;
```

Dentro de la línea del timer estamos identificando cuando pasa el medio segundo en tiempo real, en relación al **Time.deltaTime**, en este caso que el número de fotogramas del juego corresponda al medio segundo que esperamos.

Si la condición se presenta entonces aumentaremos **Minute** y si los minutos exceden 60 entonces sumaremos una hora a **Hour**. Por úlitmo si sumamos la hora reestablecemos los minutos a 0.

Las últimas dos líneas que nos falta por explicar son las de **OnMinuteChanged?.Invoke()** y **OnHourChanged?.Invoke()**, nota que están justamente después de aumentar los minutos y la hora respectivamente.

Estos métodos nos permiten lanzar un evento y decir como lo dicen los nombres de las variables que existió un cambio. Estos eventos deberán se recolectados por los objetos que estén esperando un cambio. En un momento llegaremos a esa parte pero al menos vete haciendo a la idea que el primero en esperar recibir un cambio deberá ser el TextMeshPro de nuestro juego.

Ya que tenemos el código entendido de nuestra clase vamos a guardar y compilar.

### Paso 4 Actualizar la hora con el texto

Una vez que compilamos el script vamos a realizar algunos ajustes en nuestra escena.

Primero que nada vamos a crear un objeto vacío llamado **TimeManager** al cual le añadiremos como componente nuestro script del TimeManager.

Al hacer esto nos aseguramos que tenemos un script ejecutandose en el juego sin crear realmente un objeto que ocupe recursos, esta es la estrategia por la cual existe la clase **MonoBehaviour** de Unity, así podemos crear comportamientos independientes que a partir de eventos se conecten entre sí.

Si lo aplicamos a tu proyecto podemos generar que cada cierto tiempo se actualicen las posiciones de los agentes según conforme vaya avanzando el tiempo.

Si tienes duda sobre como puedes explotar este concepto acercate con tus profesores.

![graficas](/graphics/assets/img/lab3/4_lab3.png)

Si quisieras correr el proyecto ahora mismo a nivel interfaz no pasa nada pero internamente se está disparando por la inicialización la hora a las 10:00 y desde ahí cada segundo se esta aumentando el minuto.

### Paso 5 TimeUI

Ya que tenemos preparado el **TimeManager** vamos a crear un nuevo script llamado **TimeUI**, este será el que nos ayude a actualizar nuestro TextMeshPro.

Ya que estamos dentro del script no olvides importar 

```
using TMPro;
```

Esto para el uso del TextMeshPro, recuerda haber hecho el import básico de Unitty cuando agregaste el texto a la escena.

Dentro de las varibles globales de la clase solo vamos a tener.

```
public TextMeshProUGUI timeText;
```

Para que podamos asignar nuestro TextMeshPro desde el **Inspector**.

Para esta clase no vamos a usar ni el **Start()** ni el **Update()**, por lo tanto puedes borrarlos. En su defecto usaremos los métodos **OnEnable()** y **OnDisable()**, todos 4 métodos son propios de la clase **MonoBehaviour** y se representan como parte del ciclo de vida de cada componente. Veremos una explicación en clase sobre esto, pero si tienes duda consulta el ciclo de vida de Unity dentro de la documentación para ver el diagrama y entender cuando se ejecuta cada método.

Dentro del método **OnEnable()** tendremos lo siguiente.

 ```
private void OnEnable()
{
    TimeManager.OnMinuteChanged += UpdateTime;
    TimeManager.OnHourChanged += UpdateTime;
}
 ```

 Y para el método **OnDisable()** tendremos lo siguiente.

```
 private void OnDisable()
{
    TimeManager.OnMinuteChanged -= UpdateTime;
    TimeManager.OnHourChanged -= UpdateTime;
}
```

Como mencionamos antes para el **TimeManager** definimos **OnMinuteChanged** y **OnHourChanged** que desde el **TimeManager** lanzan el evento del cambio de minuto y hora respectivamente.

Lo que estamos haciendo aquí es decirle a nuestro **TimeUI** que registre los eventos de estas 2 variables, entonces cuandos se notifique el evento recibamos la señal y en este caso ejecutemos la función **UpdateTime()** que añadiremos a continuación.

```
private void UpdateTime()
{
    timeText.text = $"{TimeManager.Hour.ToString("00")}:{TimeManager.Minute:00}";
}
```
La función **UpdateTime()** solo se encarga de pintar el texto de la interfaz, con los valores de la hora y minuto.

Vamos a ver otra forma de concatenar texto con la línea como la tenemos, este formato nos permite acceder a los valores de una variable dentro del mismo string. Y como adicional cuando tenemos hora o minutos menores a 10, no queremos que solo aparezca el dífito, sino que cuando hablamos de hora queremos que se ve en formato de doble dígito siendo el primero un 0. Para dar este formato podemos hacerlo de las 2 formas en las que viene descrito para las horas y minutos, ambas son equivalentes, ya eres tu quien decide cual usar.

### Paso 6 Actualizar Texto

Guardamos los cambios en **TimeUI** y ahora regresamos a Unity seleccionando nuestro TextMeshPro, dentro del texto desplegado vamos a modificarlo a que inicialmente sea **00:00**.

Por último dentro del mismo TextMeshPro vamos a añadir como componente nuestro **TimeUI**. **Aunque añaidmos el script al componente, no olvides asignar el Texto al componente del script.**

![graficas](/graphics/assets/img/lab3/6_lab3.png)
![graficas](/graphics/assets/img/lab3/7_lab3.png)

Si ejecutamos el proyecto deberiamos ver como empieza a actualizarse la interfaz con la hora correspondiente cada medio segundo.

![graficas](/graphics/assets/img/lab3/8_lab3.png)

Perfecto, ya tenemos un juego que mide su propio tiempo, ya sea que manejes el tiempo de tu juego en el servidor o de manera local ya puedes tener control del mismo para ejecutar eventos cada cierto tiempo.

### Paso 7 Eventos del cuadrado

Para empezar a ejecutar eventos y poder mover nuestro cuadrado cada cierto tiempo vamos a crear un nuevo script que se llamara **Square**.

![graficas](/graphics/assets/img/lab3/9_lab3.png)

Dentro de este script no tendremos variables globales ni imports adicionales. Lo que si tendremos es la misma inicialización de los métodos **OnEnable()** y **OnDisable()**, como se muestra a continuación.

```
public void OnEnable()
{
    TimeManager.OnMinuteChanged += TimeCheck;
}

public void OnDisable()
{
    TimeManager.OnMinuteChanged -= TimeCheck;
}
```

Puedes borrar el **Start()** y **Update()** nuevamente ya que no lo usaremos.

Ahora vamos a agregar el método **TimeCheck()**, el cual estará validando que den las 10:30 dentro del juego.

```
private void TimeCheck()
{
    if(TimeManager.Hour == 10 && TimeManager.Minute == 30)
    {
        StartCoroutine(MoveSquare());
    }
    
}
```

La parte de la validación no debe ser extraña puesto que solo valida cuando sean las 10:30 dentro del juego. La siguiente parte comienza con **StartCoroutine**, este método inicializa una corrutina, estas son funciones que permiten su ejecución y resumir desde el mismo punto desde donde se quedo la condición. Para efectos simples podemos decir que las corrutinas son funciones usadas en unity para detener la ejecución hasta que una cierta condición es alcanzada y continuan desde donde se quedaron.

La principal diferencia entre funciones y corrutinas en C# más allá de la sintáxis es que una función típica regresan cualquier valor, mientras que las corrutinas regresan un **IEnumerator** y deben usar la palabra reservada **yield** antes de hacer un **return**.

Existen 2 razones de por que usar corrutinas, la primera es para tener código asíncrono y la otra es para tener código que se ejecuta sobre muchos frames.

Así que las corrutinas nos facilitan romper el trabajo en múltiples frames, ahora bien, podrás estar pensando que esto lo podemos hacer en la función **Update()**. Aunque es cierto, recuerda que nosotros no tenemos control de dicha función. Esto hace que las corrutinas puedan ser ejecutadas bajo demanda o a una frecuencia diferente como en nuestro caso, por el lanzamiento de un evento o el tiempo de nuestro juego.

Como mencionamos las funciones que se llaman dentro de las corrutinas deben regresar un **IEnumerator** por lo tanto vamos a crear la función que nos falta **MoveSquare**, la cual actualizará nuestro cuadrado de posición.

```
private IEnumerator MoveSquare()
{
    transform.position = new Vector3(-100f,-49f,0);
    Vector3 targetPos = new Vector3(700f,-49f,0);

    Vector3 currentPos = transform.position;

    float timeElapsed = 0;
    float timeToMove = 3;

    while(timeElapsed < timeToMove){
        transform.position = Vector3.Lerp(currentPos,targetPos,timeElapsed/timeToMove);
        timeElapsed += Time.deltaTime;
        yield return null;
    }

}
```

Modifica la pocisión de vector inicial y final de los Vector3 para que se vayan alineando a tu propia interfaz.

**Nota: Si ya trabajaste en Android con Kotlin, el concepto de corrutina no te debe sonar tan nuevo, sin embargo hay un punto importante que aclarar y es que no son lo mismo en ambos lenguajes. Si bien las corrutinas de Kotlin están hechas para implementar concurrencia, no es el caso en C#, acá estan construidas para hacer más cambios en el juego por lo que su uso desmedido puede llevar a un gran consumo de recursos. En Android y en Kotlin las concurrencias en gran escala pueden ser soportadas mejor que los Threads, pero en C# debemos controlar muy bien lo que estamos haciendo para no romper nuestro juego, si tienes duda acercate con tus profesores.**

### Paso 8 Ajustes finales

Ahora ya que tenemos nuestro código completo vamos a añadir el script a nuestro cuadrado en la jerarquía y luego a como componente.

![graficas](/graphics/assets/img/lab3/10_lab3.png)

Ejecuta el proyecto y observa como el cuadrado debe pasar frente a ti.

### Paso 9 Retos adicionales

Ajusta el código para hacer que el código del cuadrado se ejecute cada 10 minutos del juego.

Ajusta el código para agregar un triángulo y que tenga su propio comportamiento con el tiempo que tu decidas.

Anexa los screenshots de tu avance y la liga del video con tu resultado final, así como tu reflexión al reporte de entrega.