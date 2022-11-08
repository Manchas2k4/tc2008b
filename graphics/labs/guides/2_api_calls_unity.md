# Llamadas API en Unity

## Objetivo
En este laboratorio exploraremos las llamadas a Interntet a través de APIs, aunque este es el contenido principal, también vamos a explorar de manera muy
simple el uso del 2D y algunos elementos de UI que ya trae Unity por default.

Vamos a hacer la implementación a la API [ChuckNorris API](https://api.chucknorris.io) y obtendremos un chiste aleatorio de la siguiente url:

```
https://api.chucknorris.io/jokes/random
```

La pequeña aplicación que vamos a crear tiene un bitón que manda llamar un nuevo chiste y al obtenerlo lo desplegaremos en pantalla a través de un componente de Texto de Unity.

## Instrucciones
Sigue los pasos descritos en la siguiente práctica, si tienes algún problema no olvides que tus profesores están para apoyarte.

## Laboratorio
### Paso 1 Crear un nuevo proyecto
Al igual que el laboratorio pasado vamos a crear una carpeta en nuestra computadora donde más nos acomodemos, y la llamaremos Lab2.

Una vez hecho esto comenzaremos a partir del UnityHub creando un nuevo proyecto.

![graficas](/graphics/assets/img/lab2/1_lab2.png)

Ahora seleccionaremos de nuestra lista un juego Core en 2D, y no olvidemos cambiar el nombre del proyecto como seleccionar la carpeta que creamos inicialmente.

![graficas](/graphics/assets/img/lab2/2_lab2.png)

Esperamos a que se haga la creación e importación inicial del proyecto, recuerda que esto puede tomar un poco de tiempo dependiendo de tu computadora.

Una vez que tenemos nuestro proyecto creado vamos a hacer un pequeño ajuste a la cámara, esto para permitir la visibilidad en nuestro modo de juego.

Como estamos en un juego 2D, los movimientos en la vista de escena son un poco diferentes, sin embargo notarás que es la misma idea, juega un poco a familiarizarte con los controles, sobre todo el zoom in y zoom out que puedes hacer con **alt+clic derecho**.

Para la cámara la dejaremos en

x = 265
y = 265
z = -10

![graficas](/graphics/assets/img/lab2/3_lab2.png)

Ahora, dentro de nuestra jerarquía vamos a agregar un botón dando clic derecho y seleccionando **UI>Legacy>Button**

![graficas](/graphics/assets/img/lab2/4_lab2.png)

Observa como se agregan varios elementos además del Botón, cuando trabajamos con estos elementos de UI sea en 2D o 3D, debemos aceptarlos, e incluso observa que un Botón contiene un elemento de Texto, esto es normal en elementos compuestos de este estilo. Puedes pensar en ello como los legos que component la UI.

![graficas](/graphics/assets/img/lab2/5_lab2.png)

Una vez que importamos es probable que te suceda algo como lo siguiente.

![graficas](/graphics/assets/img/lab2/6_lab2.png)

Tanto la cámara como los elementos del canvas esta con mucha des proporción, por lo que primero vamos a aumentar la visibilidad de la cámara.

![graficas](/graphics/assets/img/lab2/7_lab2.png)
![graficas](/graphics/assets/img/lab2/8_lab2.png)
![graficas](/graphics/assets/img/lab2/9_lab2.png)

Con esto aumentamos el tamaño de la cámara y además vamos a tratar de moverla a que quede un poco más grande que el tamaño del canvas, de momento no nos preocuparemos por medidas exactas.

Ahora seleccionaremos el botón y le daremos los siguientes parámetros.

width = 223
height = 61

Si juegas un poco con los parámetros deberás tener algo como lo siguiente.

![graficas](/graphics/assets/img/lab2/10_lab2.png)

Nota que he separado mi vista de juego de la de escena para asegurarme que la cámara muestre el botón.

**Nota: Es importante que el canvas quede dentro de la vista de cáma junto con el botón, ya que si solo es el botón, este no se mostrará por la jerarquía de elementos.**

Lo siguiente que haremos será seleccionar el **Text** que viene dentro del **Botón** y cambiaremos el nombre visible del botón como se despliega a continuación.

![graficas](/graphics/assets/img/lab2/11_lab2.png)

Ya que tenemos nuestros elementos acomodados y preparados, ahora procederemos a agregar otro texto, como podrás ver los elementos UI tienen un apartado Legacy, esto significa que dentro de poco serán modificados en futuras versiones de Unity, para el caso de los **Text** tenemos uno nuevo que se llama **Text-TextMeshPro** este será el que importemos.

![graficas](/graphics/assets/img/lab2/12_lab2.png)

Al importarlo nota el nuevo elemento en la jerarquía y también debe aparecerte una importación, aceptala y renombra el componente con el nombre de **Joke**.

![graficas](/graphics/assets/img/lab2/13_lab2.png)
![graficas](/graphics/assets/img/lab2/14_lab2.png)
![graficas](/graphics/assets/img/lab2/15_lab2.png)

Una vez con nuestro texto añadido vamos a posicionarlo debajo del botón y vamos a aumentar su tamaño a tratar de cubrir lo que resta de visibilidad de la cámara, nada exacto puede ser arbitrario.

![graficas](/graphics/assets/img/lab2/16_lab2.png)

Por último vamos al **Inspector** y modificaremos el texto inicial de nuestro Text por tre líneas continuas **---**.

![graficas](/graphics/assets/img/lab2/17_lab2.png)

Ya tenemos todos los elementos de nuestra escena, ahora comencemos con la parte de los Scripts.

Como buena práctica recuerda crear tu carpeta de Scripts dentro de tu carpeta de Assets. Y desde aquí crearemos un nuevo C# Script que se llamará **ChuckNorris**.

![graficas](/graphics/assets/img/lab2/18_lab2.png)

Una vez creado vamos a sustituir agregando primero la siguiente librería.

```
using TMPro;
```

La librería **TMPro** nos permitirá trabajar con el texto ya que viene del import adicional que hicimos cuando creamos el botón.

Dentro de la clase vamos a dejar el código de la siguiente manera.

```
public class ChuckNorris : MonoBehaviour
{
    public TextMeshProUGUI jokeText;
    public void NewJoke(){
        //Aquí agregaremos el código para llamar el API
    }
}

```

**Nota: El siguiente paso es muy importante ya que de lo contrario no podrás ver reflejado en el Inspector la función NewJoke() de la clase**

Una vez que tenemos lista nuestra clase **ChuckNorris** ahora vamos a seleccionar el **Canvas** que tenemos en la jerarquía dentro de nuestro proyecto y añadiremos el componente del Script como lo hicimos en el laboratorio pasado.

![graficas](/graphics/assets/img/lab2/19_lab2.png)

Ahora vamos a expandir el **Canvas** y seleccionaremos el Botón, dentro del **Inspector** vamos a buscar la propiedad OnClick() de este y vamos a seleccionar en el **+**.

![graficas](/graphics/assets/img/lab2/20_lab2.png)

Una vez que agregamos el elemento, vamos a seleccionar el script seleccionando el punto que aparece.

![graficas](/graphics/assets/img/lab2/21_lab2.png)

Dentro del menú que aparece debemos asegurarnos que está seleccionada la opción **scene** y dentro de esta seleccionamos nuestro **canvas**.

![graficas](/graphics/assets/img/lab2/22_lab2.png)

Para finalizar seleccionaremos de la lista donde esta la opción **No function** y buscaremos nuestro script **ChuckNorris>NewJoke()**.

![graficas](/graphics/assets/img/lab2/23_lab2.png)

**Nota: ¿Por qué no arrastramos el script como normalmente hacemos? Esto se debe a que si solo arrastramos el script desde nuestra carpeta de scripts, este archivo todavía no es una instancia creada, primero debe ser parte del juego y en este caso de nuestro canvas como componente para poder llamara a los elementos que la componen como es la función NewJoke(). Si se hace mal no verás el método de la clase.**

![graficas](/graphics/assets/img/lab2/24_lab2.png)

Ahora que tenemos la base del proyecto preparada vamos a terminar con los scripts correspondientes.

En primer lugar siempre que hablamos de conexiones hacia Bases de Datos o APIs, debemos tener en cuenta las buenas prácticas de las mismas, en este caso cuando hablamos de arquitecturas como MVC (Modelo, Vista Controlador), estamos hablando de la capa de Modelos.

Los modelos se pueden dividir en varias partes, la capa de entidades que es el modelado de los datos para hacer más fácil su acceso al momento de llamarlos. Por otro lado tenemos los Helpers, que son los conectores directos hacia el Endpoint en Internet o Local que queremos manejar.

Para nuestro caso vamos a crear una Entidad a forma de script que se llame Joke. Primero dentro de nuestra carpeta de scripts crearemos otra que se llame **Models** y dentro de esta crearemos el script **Joke**.

Como esta clase es un modelo no vamos a necesitar que herede de **MonoBehaviour**, incluso no necesitamos que tenga los imports normales.

Vamos a dejar limpia la clase de la siguiente forma.

```
public class Joke 
{
    
}
```

Ahora arriba de la declaración de la clase vamos a añadir la opción que permite manejar esta clase como una Entidad.

```
[System.Serializable]
```

Con la declaración anterior procedemos a agregar los diferentes valores que necesitemos para modelar nuestra entidad.

Aquí vamos a hacer un pequeño parentesis para revisar una cosa.

Si ejecutamos en nuestro navegador o en Postman la url

```
https://api.chucknorris.io/jokes/random
```

El resultado que obtendremos será algo como lo siguiente.

```
{
    "categories": [],
    "created_at": "2020-01-05 13:42:20.568859",
    "icon_url": "https://assets.chucknorris.host/img/avatar/chuck-norris.png",
    "id": "zSuDyeBLSg6nqCaIV_dmJQ",
    "updated_at": "2020-01-05 13:42:20.568859",
    "url": "https://api.chucknorris.io/jokes/zSuDyeBLSg6nqCaIV_dmJQ",
    "value": "Chuck Norris is my godfather. As he is yours."
}
```

Tendremos una respuesta en formato JSON, la cual contiene distintas propiedades. Si bien la que nos interesa para la práctica solamente es la de **value**, como buena práctica se recomienda mapear todo el objeto resultado.

Entonces si hacemos el ajuste en nuestra clase **Joke** el resultado quedaría algo como lo siguiente.

```
[System.Serializable]
public class Joke
{
   public string[] categories;
   public string created_at;
   public string icon_url;
   public string id;
   public string updated_at;
   public string url;
   public string value;
}
```

Entonces lo que sucederá es que cuando llamemos la url de nuestra API, como resultado vamos a generar un objeto Joke que ya contenga la información de una manera sencilla para poder trabajarla.

Ya que tenemos lista la clase **Joke** crearemos la clase **APIHelper**.

![graficas](/graphics/assets/img/lab2/25_lab2.png)

Como habrás visto en la clase **Joke** no estamos dependiendo de ninguna otra clase de Unity o del Sistema para crear la entidad. Y como mencionabamos esto nos permite modelar nuestros scripts aplicando una arquitectura MVC. Si conoces un poco sobre arquitectura puedes opnerte creativo e implementar más detalles para separar métodos. Por ejemplo: se puede implementar una meta arquitectura **Clean Architecture** para separar las clases del proyecto. 

No es objetivo del curso ver estos temas, sin embargo notemos que los elementos que conformarían las **Vistas** son todos los elementos que dependan directamente de las librerías de Unity, ya que son los que interactuan directamente con los elementos del juego.

Como la clase **APIHelper** pertenece a los modelos podemos eliminar los imports generales incluyendo el de Unity. Como en este caso haremos la llamada a Internet vamos usar algunas librerías propias de .NET.

**Nota: Existen muchas formas de hacer la llamada a Internet mediante el uso de diferentes librerías, incluso Unity propiamente tiene su forma, en otro momento veremos esto para que tengas opciones de elegir la que se te haga más simple en términos de llamadas, pero todas estas son adecuadas y pueden ser utilizadas en tu proyecto.**

Comenzando con los import tendremos.
```
using UnityEngine; //Para la clase JsonUtility
using System.Net;
using System.IO;
```
Dentro de la clase tendremos lo siguiente.

public static class APIHelper
{
    public static Joke GetNewJoke()
    {
        HttpWebRequest request = (HttpWebRequest) WebRequest.Create("https://api.chucknorris.io/jokes/random");

        HttpWebResponse response = (HttpWebResponse) request.GetResponse();

        StreamReader reader = new StreamReader(response.GetResponseStream());

        string json = reader.ReadToEnd();

        return JsonUtility.FromJson<Joke>(json);
    }
}

Ahora bien, ¿qué es lo que está pasando? 

En primer lugar estamos creando nuestro request y le estamos pasando la url de nuestra API. Como la llamada es de tipo GET, no necesitamos hacer ningún cambio.

Si más adelante necesitarás agregar campos adicionales o modificar la llamada para hacer un POST, puedes utilizar la siguiente referencia de apoyo.

[Llamadas POST](https://stackoverflow.com/questions/39246236/how-can-i-post-data-using-httpwebrequest)

Ya que declaramos nuestro request, lo mandamos llamar y obtenemos un response, el cual no tiene formato puesto que viene como string.

Para poder convertir a JSON la respuesta debemos crear un stream de lectura de la respuesta para pasar toda la información al stream y finalmente utilizaremos la clase **JsonUtility** para convertir nuestro Json y mapearlo a nuestra clase propia **Joke**.

Detente a entender bien el código puesto que esto será parte esencial de tu proyecto. Si tienes dudas pregunta a tus profesores.

El flujo ya está completo, ahora solo necesitamos terminar de conectar nuesta clase **ChuckNorris** con nuestro **APIHelper**. Si trabajaramos con una arquitectura completa MVC, aquí es donde crearíamos nuestro Controller y sobre esto haríamos la llamada en **ChuckNorris**.

Más aún, si implementaramos una **Clean Architecture** creariamos el repositorio en nuestros Modelos, después creariamos el requerimientos en la capa de Dominio y desde ahí hariamos todas las llamadas correspondientes.

Para nuestro laboratorio lo dejaremos simple. Desde **ChuckNorris** vamos a completar la función **NewJoke()** de la siguiente manera.

```
public void NewJoke(){
    Joke j = APIHelper.GetNewJoke();
    jokeText.text = j.value;
}
```
Ahora ejecutamos nuestro proyecto y damos clic en el botón de la interfaz y nada va a suceder.

Como práctica de lo que hemos hecho en todos estos laboratorios te invito a buscar el error.

Si no lo encuentras no pasa nada a continuación viene la respuesta.

Dentro de nuestra interfaz conectamos todo, incluso el script en el canvas, pero en ningún momento conectamos el **JokeText** que contiene nuestro script de **ChuckNorris**. Solo necesitamos arrastrar el texto de **Joke** al **JokeText**.

![graficas](/graphics/assets/img/lab2/26_lab2.png)

Si volvemos a ejecutar, ahora si debemos ver algo como lo siguiente.

![graficas](/graphics/assets/img/lab2/27_lab2.png)


Y listo, tenemos una interfaz conectada aun servicio API.

Recuerda que como buenas prácticas lo ideal siempre es conectar con un API cuando se trata de datos por cuestiones de seguridad. No se recomienda hacer la conexión directa hacia la BD incluso teniendo las librerías y conectores, algo que sucede por desgracias mucho en los proyectos desarrollados en .NET.

Cuida mucho estos detalles y no te olvides de la Ingeniería de Software en tu proyecto para la implementación de clases adicionales para crear una arquitectura en tu proyecto, esto será más que necesario para que cada miembro del equipo puedar participar de manera más activa en el desarrollo.