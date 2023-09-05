# Conexión con API en Android

## Objetivo

Este corto laboratorio te permitirá usar los diferentes sensores disponibles de un dispositivo Android.

## Pre-requisitos
De preferencia un dispositivo Android para poder probar los diferentes sensores y sus valores.

## Instrucciones

Sigue los pasos descritos en la siguiente práctica, si tienes algún problema no olvides que tus profesores están para apoyarte.

## Laboratorio
### Paso 1 Preparar la base del proyecto

Crea un proyecto en Android Compose como hemos hecho en los últimos laboratorios. Este paso ya debe ser familiar por lo que no entraré en detalle de como realizarlo.

### Paso 2 Introducción a los sensores en Android

El manejo de sensores en Android es algo bastante sencillo, incluso su implementación nativa sigue el mismo procedimiento para cada sensor diferente disponible.

Una de las razones por las que hemos estado utilizando Jetpack Compose es para poder hacer uso de la siguiente [librería](https://github.com/mutualmobile/ComposeSensors) que hace uso de los sensores en Android.

Esta librería facilita enormemente el manejo de los sensores pues solo basta con definirlos y se puede acceder de manera directa a los valores que regresan los mismos.

Un problema de los sensores en Android es que cada dispositivo es diferente y esto puede causar que cada fabricante agregue o modifique los sensores según el tipo de dispositivo, su gama y su hardware. Esto puede limitarte a que no todos los sensores pueden estar disponibles para usarse.

Para resolver esto la librería cuenta con el método **isAvailable()** con el cual podrás validar si puedes usar dicho sensor o no.


Para comenzar abre el archivo **build.grade** de Module:app.

![lab_3](3_sensores/3_001.jpg)

Vamos a agregar en las **dependencies** lo siguiente:

```
implementation("com.mutualmobile:composesensors:1.1.1")
```

Una vez que agregamos la librería no olvides **sincronizar** gradle para descargarla.

Después busca el archivo **MainActivity** y elimina las funciones de Compose que vienen por default, **Greeting** y **GreetingPreview**.

De la misma manera borra lo que esta dentro del componente Surface que viene por default, dejando algo como lo siguiente:

```
class MainActivity : ComponentActivity() {  
    override fun onCreate(savedInstanceState: Bundle?) {  
        super.onCreate(savedInstanceState)  
        setContent {  
            SensoresTheme {  
                // A surface container using the 'background' color from the theme  
                Surface(  
                    modifier = Modifier.fillMaxSize(),  
                    color = MaterialTheme.colorScheme.background  
                ) {  
                      
                }  
            }  
        }  
    }  
}
```

Dentro de Surface vamos a declarar el Acelerómetro de la siguiente manera:

```
val accelerometerState = rememberAccelerometerSensorState()  
Text(  
    text = "Force X: ${accelerometerState.xForce}" +  
            "\nForce Y: ${accelerometerState.yForce}" +  
            "\nForce Z: ${accelerometerState.zForce}" +  
            "\nIs Available?: ${accelerometerState.isAvailable}"  
)
```

Como puedes ver para llamar al Acelerómetro basta con llamar a la clase correspondiente de la librería, estas clases ya tienen incluido un objeto State el cual actualiza en cada cambio el valor del Sensor. Ahora bien, dentro del componente **Text** estamos imprimiendo todos los valores que nos devuelve el acelerómetro, también observa la llamada a **isAvailable** pues como mencioné, este método permite saber si tenemos acceso al sensor o no.

Una vez realizada la base del sensor, esto abre muchas posibilidades de obtención de información y generación de datos.

## Actividad
Revisa la documentación de la librería y experimenta con todas las clases incluidas, realiza un cuadro comparativo de cada sensor, para qué sirve, de que manera devuelve los datos y si está disponible para tu dispositivo.

## Reto
Con el acelerómetro del dispositivo intenta dibujar en pantalla un objeto que se mueva según la inclinación del teléfono. Utiliza la clase Canvas de Compose para realizar la tarea.

La actividad no se entrega pero ten a la mano tu tabla de comparación pues puedes llegar a necesitarla para la generación de datos en tus modelos.