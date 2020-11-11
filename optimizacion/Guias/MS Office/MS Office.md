# Matemáticas en *MS* *Office*

## Motivación

Por medio de herramientas de *Microsoft Office* como *Word* y *PowerPoint* podemos construir documentos convencionales como ensayos, cartas, contratos o presentaciones. ¿Qué hacemos cuando nuestro contenido a desarrollar debe incluir expresiones matemáticas elaboradas? Podriamos expresarlas de forma primitiva, sin prestar atención al estilo, como la siguiente formula cuadrática: x=(-b±√(b^2-4ac))/2a, pero por lo general esta forma es poco amistosa con el lector ya que es dificil de interpretar y con el autor ya que es dificil de identificar si está escrita de forma correcta. Preferiblemente, quisieramos expresar ecuaciones embebidas en el texto, como $x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}$, o en su propio renglón para dar énfasis:

$$
	x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}\text{.}
$$

Mejor aún, esta forma tipográfica de expresiones matemáticas nos permite más flexibilidad en cuanto a los símbolos que podremos utilizar. Particularmente nos interesan las operaciones sobre conjuntos como la sumatoria,

$$
	\sum_{i\in I}a_{i}x_{i}=b\text{,}
$$

que nos permiten plantear de forma generalizada hiperplanos, los cuales entendemos como restricciones o función objetivo en los modelos de programación lineal o lineal-entera.

Esta guía busca fijar convenciones para el desarrollo de informes con contenido matemático para el curso, así como dar instrucciones para trabajar de forma eficiente y dominar la composición tipográfica con *MS Office*.

## Primeros pasos

Asegurese de tener instalado la suite de *MS Office*. El procedimiento para insertar ecuaciones es aplicable en la mayoría de los programas del paquete, pero nosotros nos enfocaremos en la composición de documentos con *Word*.

Ejecute *Word* y dirijase a la pestaña del *Ribbon*, **Insertar**. Allí, coloque su cursor sobre el elemento **Ecuación**. Al tener el cursor sobre el botón, debería desplegarse una caja de texto explicando su uso. Verifique que *Word* le haya asignado un atajo de teclado (para el autor, el atajo es `Alt` + `=`).

![](./imagenes/Ecuaciones-TextBox.png)

Si no tiene un atajo asignado, puede hacerlo dirijiendose a la pestaña del *Ribbon*, **Archivo** >> **Opciones** >> **Personalizar cinta de opciones** >> **Personalizar**. Al especificar un comando, seleccione la categoría *Todos los comandos* y en comandos, *InsertarEcuación*. Teclée un atajo y verifique que haya quedado asignado. Tener un atajo asignado es importante para tener un flujo de trabajo eficiente, ya que, en el proceso de desarrollar un informe, deberá insertar muchas expresiones matemáticas.

## Estructura de informe

Por lo general, las evaluaciones del curso consisten del planteamiento de un escenario a optimizar para el cual el estudiante debe plantear un modelo de programación matemática lineal o lineal-entero. Para plantear modelos generalizados, utilizamos conjuntos, símbolos representativos de parámetros, arreglos de variables y conjuntos de restricciones. Por conveniencia para la evaluación de su entrega, recomendamos enunciar cada uno de estos componentes explicitamente. A continuación, una vista de como debe quedar su documento.

&ensp;&ensp;**Conjuntos**

&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;$I$: primer conjunto del ejemplo.

&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;$J$: segundo conjunto del ejemplo.

&ensp;&ensp;**Parámetros**

&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;$a_{ij}$: primer parámetro del ejemplo. Elemento $a$ para todo $i\in I$,$j\in J$.

&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;$b_{i}$: segundo parámetro del ejemplo. Elemento $b$ para todo $i\in I$.

&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;$c_{j}$: costos del ejemplo. Elemento $c$ para todo $j\in J$.

&ensp;&ensp;**Variables**

````{margin}
```{admonition} Nota
Si $x_{j}$ son variables binarias, podemos expresarlas con una función a trozos.
```
**Variables**

$$
	x_{j}=\begin{cases}
					1 & \text{se cumple un criterio} \\
					0 & \text{d.l.c.}
   \end{cases}\text{.}
$$

````

&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;$x_{j}$: primeras variables del ejemplo. Decisión $x$ para todo $j\in J$.

&ensp;&ensp;**Naturaleza**

````{margin}
```{admonition} Nota
NUNCA puede faltar una expresión explicita del dominio del problema (Naturaleza). Las variables pueden tomar valores en conjuntos predeterminados:
```
Algunas alternativas:

\begin{gather*}
	x_{j}\in\mathbb{R_{\geq 0}} & \forall j \in J \\
	x_{j}\in\mathbb{N} & \forall j \in J \\
	x_{j}\in\{0,1\} & \forall j \in J
\end{gather*}

````

\begin{gather*}
	x_{j}\in\mathbb{R} & \forall j \in J
\end{gather*}

&ensp;&ensp;**Restricciones**

\begin{gather*}
		\sum_{j\in J}a_{ij}x_{j}=b_{i} & \forall i\in I
\end{gather*}

> Este conjunto de restricciones nos permite identificar la región factible del problema. Este parrafo, idealmente, contendría una breve descripción de lo que representa o logra su respectivo conjunto de restricciónes.

&ensp;&ensp;**Función Objetivo**

$$
		\max\left\{ \sum_{j\in J}c_{j}x_{j}\right\}
$$

> Esta sumatoria nos permite identificar los valores de las variables de decisión que maximizan el problema según el criterio escogido. Este parrafo, idealmente, contendría una breve descripción de lo que representa o logra su respectiva función objetivo.

## Expresiones matemáticas

Veremos ahora, como escribir ecuaciones matemáticas en *Word*. En general, los símbolos tienen nombres y el programa tiene dos criterio para identificar cuando queremos insertarlos. Primero, debemos estar escribiendo dentro de un bloque de **Ecuación**; segundo, el nombre del símbolo debe indicarse con el caracter '`\`'. Por ejemplo, para insertar un simbolo $\alpha$, escribiriamos en el bloque de ecuación el código `\alpha`.

```{Warning}
INCOMPLETE SECTION.

TO-DO: Explain proper typesetting with commands. (common symbols, braces, matrices, piecewise functions and max)
```

## Ejemplo: Family Knapsack

En esta sección encontrará un posible formulación para el problema al que se habrán enfrentado en sus complementarias del knapsack familiar, donde una familia de excursionistas debe decidir qué objetos lleva cada integrante de la familia de acuerdo con ciertas restricciones adicionales. Lo importante de la siguiente formulación son los mensajes desplegables que contienen el texto tal y como se escribiría en *Word*. El texto en `esta forma`, se refiere al código que uno escribiría en los bloques de ecuación. Puede descargar este desarrollo en *Word* [aquí (pending link)](https://copa-uniandes.github.io/optimizacion/index.html).

&ensp;&ensp;**Conjuntos**

&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;$E$: conjunto de excursionistas.

&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;$O$: conjunto de objetos.

:::{admonition,dropdown,tip} ¡Click acá!
`E`: conjunto de excursionistas.

`O`: conjunto de objetos.
:::

&ensp;&ensp;**Parámetros**

&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;$b_{j}$: peso máximo que puede cargar el excursionista $j\in E$

&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;$p_{i}$: peso del objeto $i\in O$

&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;$q_{ij}$: preferencia sobre el objeto $i\in O$ del excursionista $j\in E$

:::{admonition,dropdown,tip} ¡Click acá!
`b_(j)`: peso máximo que puede cargar el excursionista `j\in E`

`p_(i)`: peso del objeto `i\in O`

`q_(ij)`: preferencia sobre el objeto `i\in O` del excursionista `j\in E`
:::

&ensp;&ensp;**Variables**

$$
	x_{ij}=\begin{cases}
					1 & \text{el objeto }i \in O\text{ es llevado por el excursionista } j\in E \\
					0 & \text{d.l.c.}
   \end{cases}
$$

:::{admonition,dropdown,tip} ¡Click acá!
`x_ij={■(1&el objeto i∈O es llevado por el excursionista j∈E@0&d.l.c.)┤`
:::

&ensp;&ensp;**Naturaleza**

\begin{gather*}
	x_{ij}\in\{0,1\} & \forall i \in O, j \in E
\end{gather*}

:::{admonition,dropdown,tip} ¡Click acá!
`x_ij\in{0,1}\forall i\in E, j\in O`
:::

&ensp;&ensp;**Restricciones**

\begin{gather*}
		\sum_{i\in O}p_{ij}x_{ij}\leq b_{j} & \forall j\in E
\end{gather*}

> Estas restricciones evitan que los objetos cargados por cada excursionista, $j\in E$, excedan su peso máximo tolerable, $b_{j}$.

:::{admonition,dropdown,tip} ¡Click acá!
`\sum_(i\in O)p_(ij) x_(ij) <= b_(j) \forall j\in E`

Estas restricciones evitan que los objetos cargados por cada excursionista, `j\in E`, excedan su peso máximo tolerable, `b_{j}`.
:::

\begin{gather*}
		\sum_{j\in E}x_{ij}=1 & \forall i\in O
\end{gather*}

> Estas restricciones garantizan que cada objeto, $i\in O$, se lleve exactamente una vez entre los excursionistas. Evita objetos repetidos o que falte algún objeto.

:::{admonition,dropdown,tip} ¡Click acá!
`\sum_(j\in E) x_(ij) =1\forall i\in O`

Estas restricciones garantizan que cada objeto, `i\in O`, se lleve exactamente una vez entre los excursionistas. Evita objetos repetidos o que falte algún objeto.
:::

&ensp;&ensp;**Función Objetivo**

$$
		\max\left\{\sum_{i\in O}\sum_{j\in E}q_{ij}x_{ij}\right\}
$$

> Esta función objetivo nos permite identificar la satisfacción total alcanzada por la familia por los objetos respectivos de cada integrante. Al maximizar la expresión, obtenemos la política óptima en cuanto a satisfacción total.

:::{admonition,dropdown,tip} ¡Click acá!
`max {\sum_(i∈O) \sum_(j∈E) (q_ij x_ij )} `

Esta función objetivo nos permite identificar la satisfacción total alcanzada por la familia por los objetos respectivos de cada integrante. Al maximizar la expresión, obtenemos la política óptima en cuanto a satisfacción total.
:::

## Siguientes pasos

Aunque *Word* es una herramienta muy versatil para la composición de documentos, resulta poco efectiva para la tipografía matemática o en la composición de documentos de investigación más formales. Para quienes buscan mayor rigor matemático, flexibilidad en el diseño de sus documentos y están dispuestos a explorar las tecnologías con las que los académicos construyen sus articulos de investigación, recomendamos aprender [*LaTeX*](https://www.overleaf.com/).

## Créditos
Equipo Principios de Optimización<br>Desarrollo: Alejandro Mantilla<br>Fecha: 10/11/2020<br>