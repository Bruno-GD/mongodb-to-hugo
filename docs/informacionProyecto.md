<<<<<<< HEAD
![](assets/Cabecera_Logo.png)
=======
![](docs/assets/Cabecera_Logo.png)
>>>>>>> 26d51f48c4a7eba5c22eb53371f77c645c33957e

# mongodb-to-hugo
Generador estático web con Hugo + MongoDB + Python

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


La metodología que hemos aplicado en el proyeto es la de scrum. En ella se basa en en la teoría de control de procesos empírica o empirismo. El empirismo asegura que el conocimiento procede de la experiencia y de tomar decisiones basándose en lo que se conoce. Scrum emplea un enfoque iterativo e incremental para optimizar la predictibilidad y el control del riesgo. Los aspectos significativos del proceso deben ser visibles para aquellos que son responsables del resultado. La transparencia requiere que dichos aspectos sean definidos por un estándar común, de tal modo que los observadores compartan un entendimiento común de lo que se está viendo.

Esta metodología está formada por 5 etapas que son:
1. Inicio
2. Planificación y estimación
3. Implementación
4. Revisión y retrospectiva
5. Lanzamiento

![](docs/assets/principios_Metodologia_Scrum.png)

Para finalizar podemos decir que la metodología Scrum es una metodología ágil que hace énfasis en el trabajo en equipo donde la claridad de los objetivos es crucial para avanzar hacia una versión cada vez mejor. Desde el punto de vista humano, favorece la motivación, la creatividad y el compromiso del equipo de trabajo. La claridad de los objetivos de cada una de las tareas programadas, así como el registro diario de las novedades, son factores que generan propuestas de avance hacia una versión mejorada. Estos factores, por supuesto, se reflejan positivamente en los niveles de producción de la empresa. Sin embargo el scrum no es muy efectivo si se hacen con grupos muy ampliados ya que se puede ir de las manos y tardar más de lo necesario. A eso, también, hay que añadirle que se tiene que trabajar con metas por días o semanales o mensuales y por etapas para poder llegar a los plazos y eso se necesita mucha organización. Asimismo es importante que las personas que hagan esta metodología tengan un gran nivel de cualificación para poder realizarla correctamente. En definitiva, el scrum si se hace bien es muy efectivo pero requiere un alto nivel de implicación.

### Analisis
- Partes interesadas
- Requisitos funcionales
- Requisitos no funcionales -> RnF_XX
- Diagnostico de casos de uso (UML)
- Posibles tecnoloías 
- Elección de tecnologías -> Matriz Requisitos/Tecnologías

### Diseño
- Mapa conceptual proyecto
- Esquema de BBDD
- Futuras pruebas a realizar

### Implementación 
- Herramientas utilizadas
- BackEnd
      - BBDD: CRUD (ejemplos + Ejemplos incorrecto ->)
- FrontEnd
  - ... 
  - ...

### Pruebas
- Futuras pruebas a realizar
- BackEnd (codigo + capturas de pantalla)
- FrontEnd

### Comparación temporal 
- Estimación inicial por tases o detallado por tereas
- Estimación real -> clockity
- Comparación temporal

### Dificultades 

### Bibliografía

[Documento repte vevops CI/CD](https://docs.google.com/document/d/1qA-qOmxmJfzvVzHCmmv_wPQ2p5U8GA0Xu0w9rMpxbSM/edit?usp=sharing)

Scrum:

- [Scrum de “Wikipedia”](https://es.wikipedia.org/wiki/Scrum_(desarrollo_de_software))
- [Metodolgia Scrum de “Softeng”](https://www.softeng.es/ca-es/empresa/metodologies-de-treball/metodologia-scrum.html)
- [Scrum de “Atlassian”](https://www.atlassian.com/es/agile/scrum)
- [Ventajas y desventajas Scrum de "Waredrew"](https://blog.wearedrew.co/ventajas-y-desventajas-de-la-metodologia-scrum)


Hugo:

- [Introducción de hugo](https://gohugo.io/getting-started/quick-start/)