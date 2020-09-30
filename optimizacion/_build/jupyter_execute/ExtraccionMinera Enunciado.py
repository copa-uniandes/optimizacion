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

Cada tonelada de carbón extraída de la zona $i\in M$ le cuesta a la empresa $c_i$ pesos.  Adicionalmente, cada zona tiene una capacidad máxima de extracción de carbón de $n_i$ toneladas. Suponga que las directivas desean explotar un mínimo de $b_j$ toneladas de cada tipo de carbón $j\in K$.    
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
Ahora considere el escenario en que la empresa incurre en un costo fijo de $q_i$ pesos cuando decide extraer carbón de la zona $i\in M$. Por lo tanto, si se decide explotar la mina $i\in M$, no se pueden extraer más de ($n_i$) toneladas de carbón. Pero si no se decide explotar, la extracción de carbón en esa zona debe ser igual a cero (0). Para esto usted debe seguir los siguientes pasos: 

### Formulación
**a.** Describa la(s) variable(s) de decisión adicional(es) que utilizará en el modelo. 


**b.** Escriba la(s) restricción(es) lineal(es) que describe(n) que si se decide explotar la mina $i\in M$, no se pueden extraer más de ($n_i$) toneladas de carbón. Pero que, si no se decide explotar, la extracción de carbón debe ser igual a cero.

**c.** Escriba la(s) restricción(es) que describe(n) la naturaleza de la(s) variable(s) adicional(es).



**e.** Escriba la función objetivo.


### Implementación
**f.** Resuelva el modelo planteado utilizando la librería de PulP en Python. ¿Cuál es la solución
óptima del problema? 



## Créditos

Desarrollo: Juan Felipe Rengifo M<br>
Fecha: 12/09/2020


```{toctree}
:hidden:
:titlesonly:


ExtraccionMinera
```
