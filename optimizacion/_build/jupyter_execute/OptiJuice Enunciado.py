# OptiJuice

## Enunciado

OptiJuice es una empresa que produce jugos. Ellos han decidido producir un nuevo conjunto de jugos autóctonos ($K$). Los jugos son una mezcla de diferentes frutas tropicales ($R$) dentro de las que se encuentran la piña, la guayaba, el níspero y el zapote. Cada uno de los tipos de jugo se diferencia de los demás en la cantidad de litros de zumo que tiene de las distintas frutas. Es por esto que, para garantizar la calidad de los jugos es necesario que el jugo del tipo $k \in K$ contenga entre un $l_{ki}$% y un $u_{ki}$% de litros de zumo de la fruta $i \in R$. Para la producción de jugos, OptiJuice tiene disponibles $b_i$ litros de zumo de la fruta $i \in R$. La compañía espera una demanda mínima de $d_k$ litros y desea vender cada litro de jugo del tipo $k \in K$ a $p_k$ pesos. 

Usted debe formular un programa lineal que le permita OptiJuice responder la siguiente pregunta: ¿Cuántos litros de zumo de cada fruta se deben mezclar para producir cada uno de los tipos de jugos, de manera que se cumplan las condiciones previamente expuestas y se maximicen los ingresos totales?

## Formulación

**a.** Describa la(s) variable(s) de decisión que utilizará en el modelo. 



**b.** Escriba la(s) restricción(es) lineal(es) que describe(n) que el jugo del tipo $k\in K$ debe contener entre un $l_{ki}$% y un $u_{ki}$% de litros de zumo de la fruta $i\in R$. 


**c.** Escriba la(s) restricción(es) que describe(n) que OptiJuice puede utilizar máximo $b_i$ litros de zumo de la fruta $i\in R$. 


**d.** Escriba la(s) restricción(es) que describe(n) que OptiJuice desea cumplir con la demanda mínima de $d_k$ litros jugo del tipo $k\in K$. 


**e.** Escriba la(s) restricción(es) que describe(n) matemáticamente el tipo de variable(s) que está utilizando dentro del modelo. 


**f.** Escriba la función objetivo que maximiza los ingresos totales.


## Implementación

**g.** Resuelva el modelo planteado utilizando la librería de PulP en Python. ¿Cuál es la solución
óptima del problema? 



## Créditos

Desarrollo: Juan Felipe Rengifo M<br>
Fecha: 05/09/2020


```{toctree}
:hidden:
:titlesonly:


OptiJuice
```
