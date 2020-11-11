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
&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;$a_{ij}$: primer parámetro del ejemplo. Elemento $a$ para todo $i\in I$,$j\in J$
&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;$b_i$: segundo parámetro del ejemplo. Elemento $b$ para todo $i\in I$
&ensp;&ensp;**Variables**
&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;$x_{ij}$: primeras variabels del ejemplo. Decisión $x$ para todo $i\in I$,$j\in J$
```{margin} An optional title
Si $x_{ij}$ son variables binarias, podemos expresarlas con la siguiente función a trozos.
```
&ensp;&ensp;**Variables**
$$
	x_{ij}=\begin{cases}
					1 & \text{si se cumple una condición} \\
					0 & \text{d.l.c.}
   \end{cases}
$$
&ensp;&ensp;**Naturaleza**
```{margin}
NUNCA puede faltar una expresión explicita del dominio del problema (Naturaleza). Las variables pueden tomar valores en conjuntos predeterminados:
```
$$
	x_{ij}\in\mathbb{R}\forall i\in I, j \in J
$$
ó
$$
	x_{ij}\in\mathbb{R_{\geq 0}}\forall i\in I, j \in J
$$
ó
$$
	x_{ij}\in\mathbb{N}\forall i\in I, j \in J
$$
ó
$$
	x_{ij}\in\{0,1\}\forall i\in I, j \in J
$$
&ensp;&ensp;**Restricciones**

&ensp;&ensp;**Función Objetivo**
## Expresiones matemáticas

All your files and folders are presented as a tree in the file explorer. You can switch from one to another by clicking a file in the tree.

## Ejemplo: 1D Bin Packing


