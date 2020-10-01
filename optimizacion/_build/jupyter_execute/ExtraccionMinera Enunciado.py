# Extracción minera

## Punto 1

### Enunciado
La minería de cielo abierto es una actividad industrial que consiste en remover grandes cantidades de suelo para extraer el mineral deseado. Este tipo de minas son comunes en la extracción de materiales como: arena, arcilla, cobre y carbón. Las directivas de una empresa de extracción minera desean explotar un conjunto de zonas ($M$), de las cuales se puede extraer un conjunto de diferentes tipos de carbón ($K$). Se sabe que de la zona $i\in M$ sólo puede extraerse el carbón tipo $j\in K$. Para ello, suponga que $a_{ij}$ es un parámetro binario que toma el valor de 1 si en la zona $i\in M$ se puede extraer carbón del tipo $j\in K$ y 0 en el caso contrario. La Figura 1 presenta un ejemplo en el cual hay 36 zonas y 4 tipos de carbón. Por ejemplo, para la zona uno se tiene que $a_{11}=0$, $a_{12}=1$, $a_{13}=0$ y $a_{14}=0$ ya que de la zona 1 sólo puede extraerse el tipo de carbón 2 (hulla). 

*Figura 1:*
<table>
  <tr id="ROW1">
	<td style="text-align:center; background-color: lightblue">1</td>
	<td style="text-align:center; background-color: lightblue">2</td>
	<td style="text-align:center; background-color: green">3</td>
    <td style="text-align:center; background-color: green">4</td> 
    <td style="text-align:center; background-color: lightblue">5</td>
    <td style="text-align:center; background-color: green">6</td>
  </tr>
  <tr id="ROW2">
	<td style="text-align:center; background-color: lightblue">7</td>
	<td style="text-align:center; background-color: lightblue">8</td>
	<td style="text-align:center; background-color: purple">9</td>
    <td style="text-align:center; background-color: purple">10</td> 
    <td style="text-align:center; background-color: lightblue">11</td>
    <td style="text-align:center; background-color: green">12</td>
  </tr>
  <tr id="ROW3">
	<td style="text-align:center; background-color: purple">13</td>
	<td style="text-align:center; background-color: green">14</td>
	<td style="text-align:center; background-color: green">15</td>
    <td style="text-align:center; background-color: lightblue">16</td> 
    <td style="text-align:center; background-color: lightblue">17</td>
    <td style="text-align:center; background-color: green">18</td>
  </tr>
  <tr id="ROW4">
	<td style="text-align:center; background-color: purple">19</td>
	<td style="text-align:center; background-color: red">20</td>
	<td style="text-align:center; background-color: green">21</td>
    <td style="text-align:center; background-color: purple">22</td> 
    <td style="text-align:center; background-color: purple">23</td>
    <td style="text-align:center; background-color: purple">24</td>
  </tr>
  <tr id="ROW5">
	<td style="text-align:center; background-color: purple">25</td>
	<td style="text-align:center; background-color: green">26</td>
	<td style="text-align:center; background-color: green">27</td>
    <td style="text-align:center; background-color: red">28</td> 
    <td style="text-align:center; background-color: red">29</td>
    <td style="text-align:center; background-color: red">30</td>
  </tr>
  <tr id="ROW6">
	<td style="text-align:center; background-color: lightblue">31</td>
	<td style="text-align:center; background-color: green">32</td>
	<td style="text-align:center; background-color: lightblue">33</td>
    <td style="text-align:center; background-color: purple">34</td> 
    <td style="text-align:center; background-color: red">35</td>
    <td style="text-align:center; background-color: purple">36</td>
  </tr>
</table>
<br>
<table>
  <tr id="ROW1">
	<td style="text-align:center; background-color: purple">Antracita</td>
	<td style="text-align:center; background-color: lightblue">Hulla</td>
	<td style="text-align:center; background-color: green">Turba</td>
    <td style="text-align:center; background-color: red">Lignito</td> 
  </tr>
</table>

Cada tonelada de carbón extraída de la zona $i\in M$ le cuesta a la empresa $c_i$ pesos.  Adicionalmente, cada zona tiene una capacidad máxima de extracción de carbón de $n_i$ toneladas. La Tabla 1 muestra la información de capacidades máximas y costos para cada zona.

<p style="text-align: center;"><b>Tabla 1. Información de extracción de cada zona</b></p>

|Zona|Capacidad máxima de extracción de carbón (ton)|Costo por tonelada de carbón extraído ($)|
|:--:|:--------------------------------------------:|:--------------------------------------:|
|1|189|16|
|2|196|6|
|3|143|11|
|4|136|8|
|5|106|5|
|6|151|25|
|7|170|16|
|8|129|17|
|9|184|25|
|10|122|8|
|11|146|15|
|12|190|8|
|13|160|10|
|14|109|20|
|15|133|6|
|16|198|17|
|17|138|6|
|18|107|20|
|19|117|5|
|20|150|8|
|21|171|25|
|22|103|11|
|23|157|8|
|24|143|7|
|25|170|7|
|26|130|28|
|27|140|26|
|28|126|27|
|29|180|9|
|30|153|24|
|31|108|15|
|32|132|14|
|33|105|22|
|34|145|20|
|35|145|19|
|36|114|8|

<br>

Por último. Suponga que las directivas desean explotar un mínimo de $b_j$ toneladas de cada tipo de carbón $j\in K$. La Tabla 2 presenta dichas cantidades.

<p style="text-align: center;"><b>Tabla 2. Requerimiento mínimo de cada tipo de carbón</b></p>

|Tipo de carbón|Mínimo de toneladas a explotar|
|:------------:|:----------------------------:|
|Antracita|862|
|Huila|898|
|Turba|562|
|Lignito|742|

<br> 
Usted debe formular un programa lineal que le permita a la empresa decidir cuánto deben extraer en cada zona de manera que se cumplan los requerimientos a un mínimo costo. Para esto usted debe seguir los siguientes pasos: 

### Formulación
**a.** Describa la(s) variable(s) de decisión que utilizará en el modelo. 


**b.** Escriba la(s) restricción(es) lineal(es) que describe(n) la cantidad de carbón extraído del tipo $j\in K$, debe como mínimo $b_j$.    


**c.** Escriba la(s) restricción(es) lineal(es) que describe(n) que no se pueden extraer más de ($n_i$) toneladas de carbón en la zona $i\in M$.   


**d.** Escriba la(s) restricción(es) que describe(n) la naturaleza de la(s) variable(s) incluida(s) en el modelo. 


**e.** Escriba la función objetivo.


### Implementación
**g.** Resuelva el modelo planteado utilizando la librería de PulP en Python. ¿Cuál es la solución
óptima del problema? 



## Punto 2

### Enunciado
Ahora considere el escenario en que la empresa incurre en un costo fijo de $q_i$ pesos cuando decide extraer carbón de la zona $i\in M$. Por lo tanto, si se decide explotar la mina $i\in M$, no se pueden extraer más de ($n_i$) toneladas de carbón. Pero si no se decide explotar, la extracción de carbón en esa zona debe ser igual a cero (0). La Tabla 3 presenta la información sobre los costos fijos de extraer cada zona. 
<br>

<p style="text-align: center;"><b>Tabla 3. Costo fijo por extracción para cada zona</b></p>

|Zona|Costo fijo de extracción en la zona|
|:--:|:---------------------------------:|
|1|240|
|2|155|
|3|240|
|4|125|
|5|177|
|6|342|
|7|157|
|8|457|
|9|396|
|10|411|
|11|341|
|12|469|
|13|402|
|14|186|
|15|404|
|16|344|
|17|290|
|18|340|
|19|482|
|20|472|
|21|394|
|22|102|
|23|330|
|24|433|
|25|205|
|26|394|
|27|156|
|28|298|
|29|134|
|30|462|
|31|432|
|32|362|
|33|127|
|34|203|
|35|417|
|36|215|




Para esto usted debe seguir los siguientes pasos: 

### Formulación
**a.** Describa la(s) variable(s) de decisión adicional(es) que utilizará en el modelo. 


**b.** Escriba la(s) restricción(es) lineal(es) que describe(n) que si se decide explotar la mina $i\in M$, no se pueden extraer más de ($n_i$) toneladas de carbón. Pero que, si no se decide explotar, la extracción de carbón debe ser igual a cero.

**c.** Escriba la(s) restricción(es) que describe(n) la naturaleza de la(s) variable(s) adicional(es).



**e.** Escriba la función objetivo.


### Implementación
**f.** Resuelva el modelo planteado utilizando la librería de PulP en Python. ¿Cuál es la solución
óptima del problema? 



## Créditos

Equipo Principios de Optimización<br>
Instancia: Juan Felipe Rengifo M<br>
Fecha: 30/09/2020


```{toctree}
:hidden:
:titlesonly:


ExtraccionMinera
```
