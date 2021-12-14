![](assets/Cabecera_Logo.png)
![](assets/logoMopygo.png)

# Índice
<!-- Poner índice -->
# Introducción

En este proyecto tendremos que actualizar una web de una empresa de menus de restaurantes de lujo. La página web contine listas de cartas de restaurentes (ítems) que están en stock, en las cuales estas se clasifican en diferentes estilo de cocina.

El objetivo es implementar un sistema de integración y entrega contínua (CI/CD), y a traves de python se desarrollará una aplicación para poder extraer los datos de MongoAtlas.

Por otra parte se tranformará los documentos JSON a un ficheros Markdown a traves de una aplicación de Python. A continuación esos ficheros se tienen que meter en una estructura de directorio que establece el generador de sitios estáticos llamado "Hugo" a traves de otra aplicacón de Python. "Hugo" leerá los ficheros Markdown y los transformará en documentos HTML que previamente los usaremos para la "nueva web". Finalmnte se creará el CSS.

EL objetivo de este proyecto es facilitar al comprador y cada vez que se añade, se actualice o se elimine ítem de la base de datos de forma automática con la nueva información actualizada sin necesidad de acceder al Wordpress.

Requisitos: 
- El sistema se tiene que desplegar de manera automática mediante Docker.
- Incrementar un sistema _workflow_ en git.
- Aplicar el método SOLID.
- Documentar el manual técnico que descrbe la arquitectura de la aplicación. 

### Metodología

Desarrollo iterativo y creciente (o incremental) es un proceso de desarrollo de software creado en respuesta a las debilidades del modelo tradicional de cascada.

Básicamente este modelo de desarrollo, que no es más que un conjunto de tareas agrupadas en pequeñas etapas repetitivas (iteraciones), es uno de los más utilizados en los últimos tiempos ya que, como se relaciona con novedosas estrategias de desarrollo de software y una programación extrema, es empleado en metodologías diversas.

El modelo consta de diversas etapas de desarrollo en cada incremento, las cuales inician con el análisis y finalizan con la instauración y aprobación del sistema.

El modelo incremental lleva a pensar en un desarrollo modular, con entregas
parciales del producto Software denominados "incrementos" del sistema, que son escogidos en base a prioridades predefinidas de algún modo.

El modelo permite una implementación con refinamientos sucesivos (ampliación y/o mejoras). Con cada incremento se agrega nueva funcionalidad o se cubren nuevos requisitos o bien se mejora la versión previamente implementada del producto software.

![](assets/incremental.png)

En definitiva este modelo es más flexible y rápido de usar. Además de reducir las propiedades de riesgo por lo que reduce tanto el coste de producción como el tiempo de creación. También es más fácil de probar y de depurar en una iteración más pequeña eso nos facilita detectar errores en porciones más pequeñas del código. Gracias a esto le permite al usuario utilizar el sistema antes de su puesta en producción ya que todas las piezas del mismo han sido probadas y funcionan.

No obstante, hay que tener en cuenta que se requiere una cierta experiencia y que las fases de iteraciones no se superponen por lo que no podemos reutilizar iteraciones, creando así un aumento considerable del código. Así mismo hay que considerar que este método puede ocasionar problemas de la arquitectura.

En conclusión dependiendo de la finalidad de cada proyecto nos puede beneficiar este método ya que es más rápido, flexible y no hay que olvidar que reduce el coste de producción.



Además nos hemos apoyado con el scrum. En ella se basa en en la teoría de control de procesos empírica o empirismo. El empirismo asegura que el conocimiento procede de la experiencia y de tomar decisiones basándose en lo que se conoce. Scrum emplea un enfoque iterativo e incremental para optimizar la predictibilidad y el control del riesgo. Los aspectos significativos del proceso deben ser visibles para aquellos que son responsables del resultado. La transparencia requiere que dichos aspectos sean definidos por un estándar común, de tal modo que los observadores compartan un entendimiento común de lo que se está viendo.

Esta metodología está formada por 5 etapas que son:
1. Inicio
2. Planificación y estimación
3. Implementación
4. Revisión y retrospectiva
5. Lanzamiento

![](assets/principios_Metodologia_Scrum.png)

Para finalizar podemos decir que Scrum es una metodología ágil que hace énfasis en el trabajo en equipo donde la claridad de los objetivos es crucial para avanzar hacia una versión cada vez mejor. Desde el punto de vista humano, favorece la motivación, la creatividad y el compromiso del equipo de trabajo. La claridad de los objetivos de cada una de las tareas programadas, así como el registro diario de las novedades, son factores que generan propuestas de avance hacia una versión mejorada. Estos factores, por supuesto, se reflejan positivamente en los niveles de producción de la empresa. Sin embargo el scrum no es muy efectivo si se hacen con grupos muy ampliados ya que se puede ir de las manos y tardar más de lo necesario. A eso, también, hay que añadirle que se tiene que trabajar con metas por días o semanales o mensuales y por etapas para poder llegar a los plazos y eso se necesita mucha organización. Asimismo es importante que las personas que hagan esta metodología tengan un gran nivel de cualificación para poder realizarla correctamente. En definitiva, el scrum si se hace bien es muy efectivo pero requiere un alto nivel de implicación.

### Analisis
<!-- - Partes interesadas
- Requisitos funcionales
- Requisitos no funcionales -> RnF_XX
- Diagnostico de casos de uso (UML) -->
- Posibles tecnoloías 
- Elección de tecnologías -> Matriz Requisitos/Tecnologías

### Diseño
- Mapa conceptual proyecto
![](assets/arquitectura.png)
<!-- Explicarlo detalladamente -->

- Esquema de BBDD

Cada coleccion es un tipo de restaurante, dentro de ella está la listas de los restaurentes.
En cada documento sigue una estructura con los datos del restaurantes como por ejemplo el nombre del
restaurante, la ubicación, la capacidad del local.

```json
{
  $jsonSchema: {
    bsonType: 'object',
    required: [
      'name',
      'location',
      'price',
      'menu',
      'capacity'
    ],
    properties: {
      name: {
        bsonType: 'string'
      },
      location: {
        bsonType: 'string'
      },
      price: {
        bsonType: 'int'
      },
      capacity: {
        bsonType: 'int'
      },
      menu: {
        bsonType: 'array',
        items: {
          additionalProperties: false,
		  required: [
            'menuName',
            'first',
            'second',
            'desert'
          ],
          properties: {
            menuName: {
              bsonType: 'string'
            },
            first: {
              bsonType: 'string'
            },
            second: {
              bsonType: 'string'
            },
            desert: {
              bsonType: 'string'
            }
          }
        }
      }
    }
  }
}

```
Cada documento 

- Futuras pruebas a realizar
<!-- quierres casos test o quieres un video de comporvando de como se hace el TDD 
expliaccaion de cada caso test-->

### Implementación 

- Tecnologías utilizadas

Las tecnologías utilizadas en MOPYGO son las siguientes:
## GoHugo

**GoHugo** es un framework para creación de sitios web de propósito general, además de ser generadores de sitios 
estáticos. 

## MongoDB

El **MongoDB** es un sistema de base de datos NoSQL, orientado a documentos y de código abierto


- Herramientas utilizadas

Las herramientas utilizadas en MOPYGO son las siguientes:

## VsCode

El **VsCode** es un editor de código fuente (IDE) utilizado para desarrollar el código fuente. El cual podemos 
usar las erramientas como conventional commits, live Share, git graph, Python.

## Git

El **Git** es un software de control de versiones. En nuestro caso hemos utilizado Git como sistema de versionado
de código para compartir y trabajar sobre nuestra aplicación y para mantener un registro de los cambios realizados.

## Clockify

El **Clockify** es una aplicación simple de seguimiento del tiempo y planilla de horarios que permiten tanto 
al usuario como a un equipo de trabajorealizar el seguimiento de las horas trabajadas en los proyectos. 

## GitHub

El **GitHub** es una forja para alojar proyectos utilizando el sistema de control de versiones Git. Lo hemos
utilizado esta plataforma para almacenar nuestro proyecto en la nube y además hemos utilizado la rama de github
pages para hostear nuestra web en la red.

## Black 
_Black_ es un formateador obstinado que cumple con los requisitos impuestos en [PEP 8](https://www.python.org/dev/peps/pep-0008/). _Black_ reformatea archivos completos en su lugar. Las opciones de configuración de estilo están deliberadamente limitadas y rara vez se agregan. No tiene en cuenta el formato anterior.

## Coverage 
_Coverage_ es una herramienta para medir la cobertura de código de los programas Python. Supervisa su programa, observa qué partes del código se han ejecutado, luego analiza la fuente para identificar el código que podría haberse ejecutado pero no lo ha sido.

La medición de cobertura se usa generalmente para medir la efectividad de las pruebas. Puede mostrar qué partes de su código están siendo ejercitadas por pruebas y cuáles no.

- BackEnd
<!-- Como te ponemos la bd. python, hugo  -->

- BBDD: CRUD (ejemplos + Ejemplos incorrecto ->)
- FrontEnd
<!-- lo que ve el usuario Site capturas iria bien de pa pag web? -->
  - ... 
  - ...

### Pruebas <!-- pruebas realizadas con el TDD -->
- Futuras pruebas a realizar
- BackEnd (codigo + capturas de pantalla)
- FrontEnd

### Comparación temporal 
- Estimación inicial por tases o detallado por tereas
- Estimación real -> clockity
- Comparación temporal

### Dificultades 

Las principales dificultades que hemos tenido han sido las siguientes:

En primer, lugar al no conocer la tecnología de Hugo, por lo que nos hemos tenido que documentar bastante sobre el y saber que capacidades o que cosas puede llegar a hacer este framework. Por lo que tuvimos que invertir más horas de las programadas para poder llevar a cabo los requisitos para este proyecto. 

En segundo lugar, Hugo nos ha estado dando problemas sobretodo en los dispositivos Windows y no sabias del porque. Incluso llegamos a desinstalar, volver a instalarlo y no obtuvimos ninguna respuesta. Finalmente tuvimos que cambiar el servidor web que ofrece Hugo y a partir de alli ya lo podiamos visualizar.

En tercer lugar, a medida que el proyecto iba avanzando se iba incrementando el contenido hasta llegar al punto de que en el ultimo momento ha habido modificaciones y documentacion que incrementar. 

Finalmente, el tiempo ha sido el detonante de este proyecto pues a medida que iba avanzando el proyecto veiamos que era más grande de lo que nos imaginabamos. Además a eso hay que añadir que se añadian nuevas funcionalidades y modificaciones. 



### Bibliografía

[Documento repte vevops CI/CD](https://docs.google.com/document/d/1qA-qOmxmJfzvVzHCmmv_wPQ2p5U8GA0Xu0w9rMpxbSM/edit?usp=sharing)

Scrum:

- [Scrum de “Wikipedia”](https://es.wikipedia.org/wiki/Scrum_(desarrollo_de_software))
- [Metodolgia Scrum de “Softeng”](https://www.softeng.es/ca-es/empresa/metodologies-de-treball/metodologia-scrum.html)
- [Scrum de “Atlassian”](https://www.atlassian.com/es/agile/scrum)
- [Ventajas y desventajas Scrum de "Waredrew"](https://blog.wearedrew.co/ventajas-y-desventajas-de-la-metodologia-scrum)


Hugo:

- [Introducción de hugo](https://gohugo.io/getting-started/quick-start/)