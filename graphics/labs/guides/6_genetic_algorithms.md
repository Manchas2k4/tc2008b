# Algoritmos Genéticos en Unity

## Objetivo
En este laboratorio exploraremos el concepto de algoritmos genéticos usando Unity como plataforma de visualización. 

## Instrucciones
Sigue los pasos descritos en la siguiente práctica, si tienes algún problema no olvides que tus profesores están para apoyarte.

## Laboratorio
### Paso 1 Crear y configurar un nuevo proyecto

Como de costumbre empezaremos con la creación y configuración de nuestro proyecto.

Para este laboratorio usaremos un proyecto en 2D.

![graficas](/graphics/assets/img/lab6/1_lab6.png)

Una vez que tenemos creado nuestro proyecto vamos a crear una carpeta llamada **Sprites** y en ella vamos a colocar los siguientes:

- [Block](/graphics/assets/Block.png)
- [cretin](/graphics/assets/cretin.png)

Al descargar los sprites solo necesitas colocarlos en la carpeta y de manera automática Unity los reconocerá y los visualizará en el editor.

El resultado debería verse como el siguiente.

![graficas](/graphics/assets/img/lab6/2_lab6.png)

Ahora crearemos nuestra carpeta de **Scripts** como hemos hecho en cada laboratorio.

![graficas](/graphics/assets/img/lab6/3_lab6.png)

Ahora vamos a configurar nuestra escena.

Vamos a cambiar el azul por default seleccionando la **Main Camera** y modificando en el **Inspector** la propiedad de **Background** y vamos a asignarle un color negro.

![graficas](/graphics/assets/img/lab6/4_lab6.png)

Después vamos a modificar el tamaño de la cámara a 20 unidades.

![graficas](/graphics/assets/img/lab6/5_lab6.png)

Es necesario que ajustes el zoom en la escena para que quede como se visualiza en la imagen.

Ahora desde nuestra carpeta de **Sprites** vamos a añadir 2 **Block**.

![graficas](/graphics/assets/img/lab6/6_lab6.png)

El tamaño de los bloques es un poco grande para lo que queremos realizar así que vamos a ajustar el tamaño del sprite.

Desde el **Inspector** teniendo seleccionado el Sprite de **Block** vamos a ver que tenemos la propiedad **Pixels Per Unit**, esto lo vamos a ajustar de los 100 que trae por default a 250. Una vez que tenemos la selección debemos dar clic en **Apply** para que se apliquen los cambios a nuestros sprites añadidos a la escena.

![graficas](/graphics/assets/img/lab6/7_lab6.png)

Ahora vamos a renombrar los sprites de la escena.

El que tenemos más arriba a la derecha lo llamaremos **Target** y cambiaremos su color a rojo.

![graficas](/graphics/assets/img/lab6/8_lab6.png)

Para el segundo lo llamaremos **SpawnPoint** y le asignaremos el color azul.

![graficas](/graphics/assets/img/lab6/9_lab6.png)

Ahora simplemente vamos a acomodar los dos sprites a tratar que estén lo más esquinados posibles, pero no tanto que esten pegados al borde.

El acomodo es arbitrario así que no te preocupes por las coordenadas exactas.

![graficas](/graphics/assets/img/lab6/10_lab6.png)

Listo. Con esto ya tenemos configurada la base de nuestra escena y proyecto. Ahora seguiremos con los Scripts.

### Paso 2 Generación de Scripts

Para este laboratorio necesitaremos 3 scripts, que podemos ir creando de una vez e iremos modificando poco a poco.

Los scripts a crear son los siguientes:

1. GeneticPathFinder
2. PopulationController
3. DNA

![graficas](/graphics/assets/img/lab6/11_lab6.png)

### Paso 3 Clase DNA

Abriremos nuestro editor y nos iremos de lleno a la clase DNA.

Para el ejemplo tan simple que manejaremos quizás no sea necesaria la clase **DNA** pero como siempre queremos estructurar lo mejor posible nuestro programa.

Antes de comenzar con el script te dejaré un pequeño resumen de para que sirve cada clase.

**GeneticPathFinder**: Puedes verlo como nuestra criatura, esta contiene el algoritmo que permite moverse a través del mapa y en este caso buscar llegar al objetivo.

**PopulationController**: Este es un generador global del juego que maneja cuando una población está viva, cada vez que muera la población se encarga de generar una nueva y continuar haciendolo de manera infinita.

**DNA**: Esta clase contiene los componentes que integran una criatura, en este caso una lista de **Vector2**, es con esto que una criatura sabe hacia donde tiene que moverse.

Entonces para continuar en nuestro scripts de la clase **DNA** vamos a eliminar el método **Start()** y el  **Update()**. A su vez quitamos la declaración de herencia del **MonoBehaviour**.

```
public class DNA : MonoBehaviour
{
    
}
```

Dentro de las variables globales de la clase vamos a declarar la lista de **Vector2** que como mencionaba antes servirá para que la criatura se pueda mover.

```
public List<Vector2> genes = new List<Vector2>();
```

Después vamos a declarar un constructor, que servirá como constructor inicial para cuando no tengamos una población previa, es decir, nuestro caso inicial.

```
public DNA(int genomeLength = 50)
{
    for(int i = 0; i < genomeLength; i++)
    {
        genes.Add(new Vector2(Random.Range(-1.0f,1.0f),Random.Range(-1.0f,1.0f)));
    }
}
```

Si analizamos el código observaremos que para el caso inicial vamos a crear 50 genes para cada criatura. Estos contendrán los **Vector2** con coordenadas aleatorias.

Ahora vamos a añadir otro constructor, el cual nos permitirá trabajar cuando se haga la combinación de genes de una población que esté evolucionando.

Piensa en ello como la parte tal cual funcionan los cromosomas en los seres humanos, donde se tienen los cromosomas del padre y los cromosomas de la madre y de alguna manera se heredan a un hijo.

Si bien este proceso no sabemos como ocurre en la naturaleza, nosotros lo imitaremos usando aleatorios, es decir en primer lugar veremos si es necesario crear nuevos genes completamente, o en su defecto tomar alguno de los genes ya sea del padre o de la madre.

```
public DNA(DNA parent,DNA partner,float mutationRate=0.01f)
    {
        for(int i = 0; i < parent.genes.Count; i++)
        {
            float mutationChance = Random.Range(0.0f,1.0f);
            if(mutationChance < mutationRate)
            {
                genes.Add(new Vector2(Random.Range(-1.0f,1.0f),Random.Range(-1.0f,1.0f)));
            }
            else
            {
                int chance = Random.Range(0,2);
                if(chance == 0)
                {
                    genes.Add(parent.genes[i]);
                }
                else
                {
                    genes.Add(partner.genes[i]);
                }
            }
        }
    }
```

El código es un poco extenso pero es bastante sencillo, nota las variables de **mutationChance** para saber si hay probabilidad de crear nuevos genes desde 0 o si se utilizan los genes de los progenitores.

Con esto tenemos nuestra clase **DNA** no necesitamos hacerle nada más.

Ahora pasaremos al script de **GeneticPathFinder**.

### Paso 4 Clase GeneticPathFinder

Nuevamente vamos a eliminar el método **Start()** y el **Update()**, la clase si los utilizará pero los agregaremos más adelante.

```
public class GeneticPathFinder : MonoBehaviour
{
    
}
```

Para nuestras variables globales vamos a declarar las siguientes.

```
public float creatureSpeed;
public float pathMultiplier;
int pathIndex = 0;
public DNA dna;
public bool hasFinished = false;
bool hasBeenInitialized = false;
Vector2 target;
Vector2 nextPoint;
```

Vamos a ir entendiéndolas paso a paso.

1. **creatureSpeed**: La velocidad de la criatura, la dejaremos publica para poder modificarla desde el **Inspector**.
2. **pathMultiplier**: Ayuda a mejorar la optimización de genes ya que de lo contrario el algoritmo podría estancarse en algún punto.
3. **pathIndex**: Índice actual del gen visto por la criatura, para saber como y que tanto moverse.
4. **dna**: El conjunto de genes de la criatura.
5. **hasFinished**: Bandera para saber si la criatura ha llegado a la meta.
6. **hasBeenInitialized**: Nos ayuda a saber si la criatura se ha inicializado correctamente para poder empezar su recorrido.
7. **target**: Posición final a donde tiene que llegar la criatura.
8. **nextPoint**: Siguiente punto al cual se moverá la criatura.

Una vez que tenemos nuestras variables globales vamos a crear las siguientes funciones.

```
 public void InitCreature(DNA newDna, Vector2 _target){
    dna = newDna;
    target = _target;
    nextPoint = transform.position;
    hasBeenInitialized = true;
}
```

Este método nos permite crear una nueva criatura, como la clase hereda de **MonoBehaviour** ya que es la que se visualiza en el juego, no tenemos un constructor propiamente, pero este método nos permite inicializar todo lo necesario para poder empezar.

Nota que **InitCreature** recibe como parámetros un **DNA** inicial, el cual tiene 2 opciones, o generarse de manera inicial, o de manera aleatoria por el cruce de genes, el segundo parámetro es tal cual a donde queremos que llegue.

Ahora vamos a generar el método **Update()**

```
private void Update()
{
    if(hasBeenInitialized && !hasFinished){
        if(pathIndex == dna.genes.Count)
        {
            hasFinished = true;
        }
        if((Vector2)transform.position == nextPoint)
        {
            nextPoint = (Vector2)transform.position + dna.genes[pathIndex];
            pathIndex++;
        }
        else
        {
            transform.position = Vector2.MoveTowards(transform.position,nextPoint,creatureSpeed*Time.deltaTime);
        }
    }
}
```

Lo que estamos realizando en el método **Update()** es una vez que se inicializa la criatura en cada actualización del frame:

 - Verificar si ya se ha inicializado la criatura y que no haya finalizado su recorrido.
    - En caso de que sí, entonces se verifica que el índice no haya finalizado los genes de la criatura en cuyo caso se finaliza.
    - Verificar si la criatura ya se  movió a su nueva posición, en caso de que sí, entonces se genera una nueva posición a través de la posición actual sumando alguno de los genes de la criatura que sería un movimiento entro -1 y 1 tanto en x como en y, y por últimos se aumenta el índice. 
    - En caso contrario significa que la criatura aún no se ha movido y hay que ejecutar el movimiento a la posición.

Todavía vamos a hacer ajustes en esta clase, pero para hacer una pequeña prueba vamos a añadir el método **Start()**, el cual tendrá lo siguiente.

```
public void Start()
{
    InitCreature(new DNA(),Vector2.zero);
}
```

Aquí vamos a inicializar la criatura con un **DNA** completamente nuevo y vamos a ponerle un objetivo al centro de la pantalla.

Guardamos nuestros cambios en los Scripts y regresamos a Unity.

En Unity vamos a añadir a la escena nuestro Sprite llamado **cretin** estos serán nuestras criaturas.

Al agregarlo verás que es casi un punto, esto está bien así. Ahora, mueve nuestra criatura cerca del **SpawnPoint** (cuadrado azul) y no olvides de arrastrarle a sus componentes el script de **GeneticPathFinder**. Y dentro del inspectos dejaremos las propiedades de: 

- **Creature Speed** = 10
- **Path Multiplier** = 2

![graficas](/graphics/assets/img/lab6/12_lab6.png)

Si ejecutamos nuestro proyecto veremos como la criatura se empieza a mover erráticamente hasta que en un punto se deja de mover.

Si recuerdas del código como inicialmente el número de genes son 50, lo que hacemos es dentro de todos los genes, a partir de la posición inicial empezar a mover la criatura con pasos aleatorios entre el -1 y el 1.

Hasta este punto nuestra criatura solo se mueve sin rumbo, y como solo tiene 50 genes, es practicamente imposible que logre llegar al centro de la pantalla que es el objetivo actual que tiene, mucho menos llegar al **Target** (cuadrado rojo).

Entonces, ¿Dónde está la inteligencia?.

La inteligencia viene en el siguiente paso, donde a fuerza bruta iremos haciendo que cada población avance pero usando la regla básica de la evolución, supervivencia del más apto, esto quiere decir tomaremos solo los genes de las criaturas que están más cercanas a la meta y sobre estos se hara el crossover que tenemos en nuestra clase **DNA**, en teoría, pegarle muchas veces a lo correcto eventualmente nos llevará al resultado aceptado.

En teoría esto funciona pero veamos como sucede en la práctica.

Para continuar vamos a regresar a nuestro script de **GeneticPathFinder** y vamos a añadir la variable **fitness** pero con las siguientes características para sus accesors.

```
public float fitness
{
    get
    {
        float dist = Vector2.Distance(transform.position,target);
        if(dist == 0)
        {
            dist = 0.0001f;
        }
        return 60/dist;
    }
}
```
Esta variables nos permite saber si la criatura es apta o no para pasar sus genes a la siguiente generación.

Para saber si es apta o no, primero obtenemos la distancia entre la posición actual de la criatura y el objetivo.

Después necesitamos verificar que este valor no sea 0 para evitar una división entre 0 que podría crashear nuestro programa, en caso de que fuera así, entonces lo dividimos por un valor muy pequeño.

Si solo regresaramos la distancia obtendríamos que los más alejados serían más aptos para la supervivencia, para evitar esto, invertimos este resultado haciendo la división y esto nos da como resultado que los más cercanos son los que tienen un mejor valor de aptitud para sobrevivir.

De momento es todo lo que necesitamos en el **GeneticPathFinder**. Ahora empezaremos a trabajar con nuestra población.

### Paso 5 Clase PopulationController

Abrimos el script de **PopulationController**, y nuevamente eliminamos el método **Start()** y **Update()**.

```
public class PopulationController : MonoBehaviour
{
    
}
```

Para nuestras variables globales vamos a declarar lo siguiente.

```
List<GeneticPathFinder> population = new List<GeneticPathFinder>();
public GameObject creaturePrefab;
public int populationSize = 100;
public int genomeLength;
public float cutoff = 0.3f; //how much will die or survive
public Transform spawnPoint;
public Transform end;
```

La descripción de cada variable es la siguiente:

- **population**: Es una lista de criaturas que sirven para saber que tenemos una población actual.
- **creaturePrefab**: Vamos a crear un prefab de la criatura en Unity y esa es la que se estará instanciando en cada población, la asignaremos desde el **Inspector**.
- **populationSize**: El tamaño de nuestra población por default será 100 pero podremo modificarlo desde el **Inspector**.
- **cutoff**: Esta variable nos permite saber con cuanto porcentaje de la población nos quedaremos para hacer el crossover al final de cada iteración, inicialmente es el 30% pero podemos modificarlo desde el **Inspector**.
- **spawnPoint**: Donde deben aparecer inicialmente, se asigna desde el **Inspector**.
- **end**: A donde van a llegar, se asigna desde el **Inspector**.

Ahora vamos con los métodos de la clase, en primer lugar crearemos la función **InitPopulation()** que contendrá lo siguiente.

```
void InitPopulation()
{
    for(int i =0; i < populationSize; i++)
    {
        GameObject go = Instantiate(creaturePrefab,spawnPoint.position,Quaternion.identity);
        go.GetComponent<GeneticPathFinder>().InitCreature(new DNA(genomeLength),end.position);
        population.Add(go.GetComponent<GeneticPathFinder>());
    }
}
```

Este método de forma simple según el tamaño de la población genera los objetos de nuestro prefab y les asigna la posición correspondiente.

Una vez creado el objeto se le inicializa su **DNA** pero nota que no usamos el constructor base, sino que usamos el tamaño de genoma que asignamos a la clase y el objetivo final.

Por último añadimos a la lista de la población.

Ahora crearemos el método **HasActive()**, que nos dirá si la población ha muerto o finalizado o aún sigue activa.

```
bool HasActive()
{
for(int i = 0; i <population.Count;i++)
{
    if(!population[i].hasFinished)
    {
        return true;
    }
}
return false;
}
```
Antes de pasar a la parte más importante vamos a crear la función **GetFittest**, está nos permite saber cuales criaturas son aptas para sobrevivir. Recuerda que en **GeneticPathFinder** tenemos la variable **fitness** que nos regresa que tan cerca está la criatura de la meta. 

Ahora bien, la función que vamos a agregar nos va a regresar cual de todos los elementos de la población es el que está en mejor posición o mas cerca de la meta.

```
GeneticPathFinder GetFittest()
{
    float maxFitness = float.MinValue;
    int index = 0;
    for(int i = 0; i < population.Count; i++)
    {
        if(population[i].fitness > maxFitness){
            maxFitness = population[i].fitness;
            index = i;
        }
    }
    GeneticPathFinder fittest = population[index];
    population.Remove(fittest);
    return fittest;
}
```
Ya que podemos saber que criatura es la más apta para mutarse, ahora vamos a la que en teoría es la función más compleja de todo nuestro proyecto, compleja entre comillas puesto que no es muy larga, pon atención a esta parte y revisala las veces que sea necesario, aquí es donde se realiza toda la magia o la llamada inteligencia artificial.

La función se llama **NextGeneration()** como la voy a ir explicando paso a paso vamos a declararla vacía.

```
void NextGeneration()
{

}
```
Insisto en que esta parte es la más importante, todo lo que sigue a continuación en el código, va dentro de **NextGeneration()**

Lo primero que vamos a hacer es obtener a partir del porcentaje de supervivencia, cuantos sobrevivientes totales queremos para hacer el crossover.

Esto lo haremos declarando una lista de supervivientes y una vez que tengamos el total de cuantos queremos, entonces obtendremos los más aptos usando **GetFittest()** hasta que tengamos los que necesitamos.

```
int survivorCut = Mathf.RoundToInt(populationSize*cutoff);
List<GeneticPathFinder> survivors = new List<GeneticPathFinder>();
for(int i = 0; i < survivorCut;i++)
{
    survivors.Add(GetFittest());
}
```

El siguiente paso es muy simple, dado que ya estamos llamando la siguiente generación, necesitamos destruir la generación actual, y esto empieza destruyendo los elementos en pantalla y después vaciando la lista de la población actual.

Dado que ya reservamos a nuestros sobrevivientes no pasa nada si borramos la población.

```
for(int i = 0; i < population.Count;i++)
{
    Destroy(population[i].gameObject);
}

population.Clear();
```

La siguiente es una forma un poco burda pero es para visualizar mejor lo que hacemos, vamos a iterar el total de la población que inicialmente es 0 hasta que la llenemos con el total de **populationSize**, esto es, que hayamos generado la nueva población completamente.

Esta primera iteración la hacemos con un while, dado que no sabemos cuanto nos tardaremos en generar la nueva población, eso y porque los sobrevivientes pueden y **deben** ser menores en cantidad a la población total.

Después vamos a iterar sobre cada sobreviviente y aquí vamos a crear el GameObject correspondiente para nuestra criatura.

Para la inicialización del **DNA** de la criatura pasaremos el sobreviviente actual como por llamarlo de una forma sería la madre, y después de forma aleatoria tomaremos algún otro sobreviviente que funcionaría como el padre, por último asignamos la posición final objetivo.

Recuerda que al hacer esto nuestra clase **DNA** recibe a la madre y al padre y si las chances de mutación se dan, toma ya sea alguno de los genes del padre o de la madre, o si algún gen no hace mutación crea los propios.

Aquí es donde pasa todo, ya que al dar a la nueva criatura una madre y un padre que fueron aptos para la supervivencia entonces es muy probable que el hijo reciba alguno de sus genes así como igual puede generar sus características propias no haciendolo una exacta copia de sus padres.

Este punto de no hacerlo igual es donde la naturaleza trabaja y es como tú, tienes tus propias convicciones y personalidad lo que te distingue de tus padres pero en teoría hace una mejora a la especie por que mejora en cada generación que va sucediendo.

```
while(population.Count < populationSize)
{
    for(int i = 0; i < survivors.Count;i++)
    {
        GameObject go = Instantiate(creaturePrefab,spawnPoint.position,Quaternion.identity);
        go.GetComponent<GeneticPathFinder>().InitCreature(new DNA(survivors[i].dna,survivors[Random.Range(0,10)].dna),end.position);
        population.Add(go.GetComponent<GeneticPathFinder>());
        if(population.Count >= populationSize)
        {
            break;
        }
    }
}
```

Por último ya que creamos nuestra nueva población, los sobrevivientes ya no son necesarios, por lo tanto son eliminados.

```
for(int i = 0; i < survivors.Count;i++)
{
    Destroy(survivors[i].gameObject);
}
```

Y eso es todo, acabamos de repazar la evolución de las especies con esta función, nota el poder que estamos añadiendo siguiendo la lógica de como se comporta el mundo.

Lo último que nos queda por hacer es crear las funciones **Start()** y **Update()** nuevamente.

La primera es muy sencilla puesto que solo inicializa la población 0.

```
private void Start()
{
    InitPopulation();
}
```

Para la segunda como estamos verificando en cada frame del juego, solo necesitamos checar si la población sigue activa, en caso de que no, entonces creamos una nueva generación.

```
private void Update()
{
    if(!HasActive())
    {
        NextGeneration();
    }
}
```

Vamos a guardar el script y regresamos a Unity.

### Paso 6 Ajustes del proyecto

Vamos a crear en la jerarquía un **Empty Object** al que llamaremos **PopulationControlelr** y aquí arrastraremos nuestro **Target** y nuestro **SpawnPoint**. También vamos a añadir como componente a **PopulationController** nuestro script de **PopulationController**.

![graficas](/graphics/assets/img/lab6/13_lab6.png)

Ahora vamos a crear la carpeta de **Prefabs** en nuestros **Assets** y aquí vamos a añadir nuestro objeto **cretin** y vamos a eliminar el que tenemos en la escena.

![graficas](/graphics/assets/img/lab6/14_lab6.png)

Por últimos vamos a añadir al **PopulationController** los parámetros que necesitamos de nuestro script.

- **Creature Prefab** = Al que acabamos de crear
- **Genome Length** = 50
- **Spawn Point** = Basta con arrastrar nuestro cuadrado azul, como aquí recibimos un **Transform** toma como tal la posición del mismo y no el **GameObject** como veniamos haciendo.
- **Target** = Lo mismo que con el **Spawn Point** pero usando nuestro cuadrado rojo.

La población y el cutoff lo dejaremos de momento como está.

Por último vamos a actualizar nuestro script **GeneticPathFinder** en el método **Update()**, la línea que modificaremos deberá contener lo siguiente.

```
if(pathIndex == dna.genes.Count || Vector2.Distance(transform.position,target)<0.5f)
```
Esto para saber si ya se ha llegado a la meta evitar más movimientos de esa criatura.

La función **Update()** completa es como queda a continuación.

```
  private void Update()
{
    if(hasBeenInitialized && !hasFinished){
        if(pathIndex == dna.genes.Count || Vector2.Distance(transform.position,target)<0.5f)
        {
            hasFinished = true;
        }
        if((Vector2)transform.position == nextPoint)
        {
            nextPoint = (Vector2)transform.position + dna.genes[pathIndex] * pathMultiplier;
            pathIndex++;
        }
        else
        {
            transform.position = Vector2.MoveTowards(transform.position,nextPoint,creatureSpeed*Time.deltaTime);
        }
    }
}
```

Guardamos todo, y regresamos a Unity.

Seleccionamos nuestro prefab de **cretin** y vamos a actualizar la **Creature Speed** = 50.

Y ahora sí vamos a ejecutar el proyecto.

Lo que vamos a ver es como toda nuestra población se empieza a generar y se empieza a mover, y de manera indefinida se crean nuevas generaciones cuando la anterior termina.

Pero ahora nos falta un elemento indispensable, y es que si te das cuenta, la población en sí no avanza.

Si te vas al prefab del **cretin**, verás que tiene el **Path Multiplier** = 2.

Pero si te vas al script de **GeneticPathFinder**, en ningún lugar se está usando esta variable, y es que esto es lo que permite añadir un poco más de velocidad a la simulación mejorando la forma en que se concibe el camino que debe tomar una criatura.

Vamos a actualizar el script de la siguiente forma en la función **Update()**.

```
nextPoint = (Vector2)transform.position + dna.genes[pathIndex] * pathMultiplier;
```

```
 private void Update()
{
    if(hasBeenInitialized && !hasFinished){
        if(pathIndex == dna.genes.Count)
        {
            hasFinished = true;
        }
        if((Vector2)transform.position == nextPoint)
        {
            nextPoint = (Vector2)transform.position + dna.genes[pathIndex] * pathMultiplier;
            pathIndex++;
        }
        else
        {
            transform.position = Vector2.MoveTowards(transform.position,nextPoint,creatureSpeed*Time.deltaTime);
        }
    }
}
```

Por último un pequeño detalle visual, si aún tienes el método **Start()** eliminalo, pues también este nos está bloqueando en que la población se mueva correctamente.

Salva todo y ejecuta el proyecto.

![graficas](/graphics/assets/img/lab6/15_lab6.png)

Ahora si deberías poder ver como en cada iteración, poco a poco se va moviendo la población hacia el objetivo.

Entre más iteraciones pasan, notarás que se va haciendo más lento e incluso llega un punto en que la población ya no avanza más.

Esta parte es donde necesitamos empezar a experimentar con os valores que tenemos para configurar, ya sea aumentando la cantidad de genomas de las criaturas, aumentando la población, modificando el porcentaje de cuantos son aptos en una población e incluso para velocidad de la simulación, la velocidad de las criaturas.

Hasta este punto yo dejaré la siguiente configuración.

- Population Size = 100
- Genome Length = 100
- Cutoff = 0.1
  
- Creature Speed = 200
- Path Multiplier = 3

Esto debe ser suficiente para que la población llegue al otro lado.

Como conclusiones finales podemos observar que al llegar al otro lado, parece que el conjunto de la población se alinea y ya no modifica su comportamiento.

También podemos ver una gran cantidad de criaturas se acerca como si siguieran a la población, pero realmente nunca llegan al objetivo.

Esto se debe a que recuerda que cada cambio es aleatorio, entonces aunque en teoría tienen lo genes de criaturas que sobrevivieron e incluso llegaron a la meta, son sus características propias las que lo llevan a tomar cursos diferentes, incluso puede darse el caso que se hereden genes que no sean útiles.

Llevate esta reflexión, ¿qué harías para obtener al mejor de todos? ¿sería el más rápido?,¿el que llega de alguna forma?

Tan solo si añadimos variables para declarar lo que es apto, como en la naturaleza veremos la complejidad de por que la evolución sirve pero en muchas ocasiones es cruel a lo que nosotros consideramos correcto desde un punto de vista moral.

¿Qué aplicaciones se te ocurren a lo que hemos visto?

Recuerda que Unity es una plataforma que nos permite visualizar lo que queremos expresar, no solo es un motor para desarrollar videojuegos.

Es un motor para desplegar lo que sentimos, desarrollamos y visualizamos a través del uso de gráficas computacionales.