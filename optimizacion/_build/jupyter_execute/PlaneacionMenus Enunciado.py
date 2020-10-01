# Planeación de menús

## Enunciado

El personal técnico de un hospital quiere desarrollar un sistema computarizado de planificación de
menús. Para comenzar, el hospital llevará a cabo un piloto para planificar el menú del almuerzo.
Este menú debe incluir 100 gramos (g) de cada uno de los siguientes tres grupos alimenticios ($T$): frutas,
verduras, y carnes. La siguiente tabla presenta el costo por cada 100 g de algunos alimentos sugeridos ($A$), así
como el porcentaje de macronutrientes (carbohidratos, proteínas y grasas) y la cantidad, en
miligramos (mg), de vitaminas que contienen 100 g de dichos alimentos.


| ||Vitaminas (mg)|Carbohidratos (%)| Proteína (%)| Grasas (%)|Costo (\$) por cada 100g|
|:-:|:-|-:|-:|-:|-:|-:|
|**Frutas**|||||||
||Naranja|50.00|8.90|0.80|0.00|570.00|
||Manzana|5.00|10.50|0.30|0.00|650.00|
||Banano|35.00|20.80|1.20|0.30|200.00|
||Pera|12.00|11.70|0.40|0.10|550.00|
|**Verduras**|||||||
||Brócoli|116.00|4.90|3.20|0.20|450.00|
||Espinaca|52.00|4.10|2.50|0.30|600.00|
||Guisantes|23.00|18.20|7.20|0.40|800.00|
||Pepino|9.00|0.70|0.15|2.70|500.00|
||Calabacín|21.00|7.30|4.20|0.10|450.00|
|**Carnes**|||||||
||Pollo|61.00|1.00|23.00|2.00|1,420.00|
||Res|31.00|2.00|18.00|20.00|4,800.00|
||Cerdo|2.00|1.50|16.00|27.00|2,900.00|


El menú del almuerzo debe contener una cantidad mínima de cada uno de los cuatro
macronutrientes mostrados en la tabla. Estas cantidades mínimas son: 100 mg de vitaminas, 25 g de carbohidratos, 17 g de proteínas y 5 g de grasas. El equipo técnico del hospital desea incluir un
modelo de optimización en el sistema para planear el menú del almuerzo al menor costo posible.

## Formulación
**a.** Formule matemáticamente un modelo de optimización de forma general que represente la
situación anterior. Defina clara y rigurosamente:  
- Conjuntos
- Parámetros
- Variables de decisión
- Función objetivo
- Restricciones


## Implementación

**b.** Resuelva el modelo planteado utilizando la librería de PuLP en Python. ¿Cuál es la solución
óptima del problema? 



<div style="text-align:justify"><strong>c.</strong> Varios aspectos prácticos no fueron tenidos en cuenta en el modelo planteado
anteriormente. Algunos de estos aspectos son: la inclusión de alimentos de los otros cuatro
grupos alimenticios, la planeación de menús para desayunos, almuerzos y cenas; la
planeación de menús para que los pacientes reciban menús variados de comida a lo largo
de la semana; y menús especiales para pacientes con ciertas restricciones, entre otros.
Discuta en detalle cómo podría tener en cuenta estos aspectos dentro de un modelo de
optimización en el sistema de planeación del hospital.
</div>

## Créditos

Desarrollador: Camilo Aguilar León<br>
Fecha: 08/09/2020