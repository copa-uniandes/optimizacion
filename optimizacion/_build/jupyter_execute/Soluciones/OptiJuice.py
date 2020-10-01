# Producción de jugos Solución

## Enunciado

OptiJuice es una empresa que produce jugos. Ellos han decidido producir un nuevo conjunto de jugos autóctonos ($K$). Los jugos son una mezcla de diferentes frutas tropicales ($R$) dentro de las que se encuentran la piña, la guayaba, el níspero y el zapote. Cada uno de los tipos de jugo se diferencia de los demás en la cantidad de litros de zumo que tiene de las distintas frutas. Es por esto que, para garantizar la calidad de los jugos es necesario que el jugo del tipo $k \in K$ contenga entre un $l_{ki}$% y un $u_{ki}$% de litros de zumo de la fruta $i \in R$. Para la producción de jugos, OptiJuice tiene disponibles $b_i$ litros de zumo de la fruta $i \in R$. La compañía espera una demanda mínima de $d_k$ litros y desea vender cada litro de jugo del tipo $k \in K$ a $p_k$ pesos. La información mencionada se presenta en las Tablas 1 a 4. 


<p style="text-align: center;"><b>Tabla 1. Mínimo porcentaje de las frutas en los jugos</b></p>

<table class="egt">
    
  <tr>  
    <th>Mínimo porcentaje</th> 
    <th colspan="5";style="text-align:center">Frutas</th>
  </tr>
    
  <tr>
    <th style="text-align:center">Jugos</th>
    <td style="text-align:center"><i>Piña (%)</i></td>
    <td style="text-align:center"><i>Guayaba (%)</i></td>
    <td style="text-align:center"><i>Nispero (%)</i></td>
    <td style="text-align:center"><i>Zapote (%)</i></td>
  </tr>

  <tr>
    <td style="text-align:left"><i>Saludable</i></td>
    <td style="text-align:center">32</td>
    <td style="text-align:center">27</td>
    <td style="text-align:center">12</td>
    <td style="text-align:center">13</td>
  </tr>
    
  <tr>
    <td style="text-align:left"><i>Tropical</i></td>
    <td style="text-align:center">18</td>
    <td style="text-align:center">30</td>
    <td style="text-align:center">31</td>
    <td style="text-align:center">34</td>
  </tr>
    
  <tr>
    <td style="text-align:left"><i>Mañanero</i></td>
    <td style="text-align:center">7</td>
    <td style="text-align:center">31</td>
    <td style="text-align:center">28</td>
    <td style="text-align:center">22</td>
  </tr>

  <tr>
    <td style="text-align:left"><i>Colombiano</i></td>
    <td style="text-align:center">11</td>
    <td style="text-align:center">5</td>
    <td style="text-align:center">15</td>
    <td style="text-align:center">18</td>
  </tr>
    
  <tr>
    <td style="text-align:left"><i>Refrescante</i></td>
    <td style="text-align:center">46</td>
    <td style="text-align:center">50</td>
    <td style="text-align:center">2</td>
    <td style="text-align:center">43</td>
  </tr>
    
  <tr>
    <td style="text-align:left"><i>Light</i></td>
    <td style="text-align:center">36</td>
    <td style="text-align:center">19</td>
    <td style="text-align:center">14</td>
    <td style="text-align:center">40</td>
  </tr>
    
</table>

<p style="text-align: center;"><b>Tabla 2. Máximo porcentaje de las frutas en los jugos</b></p>

<table class="egt">
    
  <tr>  
    <th>Máximo porcentaje</th> 
    <th colspan="5";style="text-align:center">Frutas</th>
  </tr>
    
  <tr>
    <th style="text-align:center">Jugos</th>
    <td style="text-align:center"><i>Piña (%)</i></td>
    <td style="text-align:center"><i>Guayaba (%)</i></td>
    <td style="text-align:center"><i>Nispero (%)</i></td>
    <td style="text-align:center"><i>Zapote (%)</i></td>
  </tr>

  <tr>
    <td style="text-align:left"><i>Saludable</i></td>
    <td style="text-align:center">95</td>
    <td style="text-align:center">83</td>
    <td style="text-align:center">66</td>
    <td style="text-align:center">87</td>
  </tr>
    
  <tr>
    <td style="text-align:left"><i>Tropical</i></td>
    <td style="text-align:center">92</td>
    <td style="text-align:center">76</td>
    <td style="text-align:center">69</td>
    <td style="text-align:center">56</td>
  </tr>
    
  <tr>
    <td style="text-align:left"><i>Mañanero</i></td>
    <td style="text-align:center">81</td>
    <td style="text-align:center">61</td>
    <td style="text-align:center">28</td>
    <td style="text-align:center">94</td>
  </tr>

  <tr>
    <td style="text-align:left"><i>Colombiano</i></td>
    <td style="text-align:center">82</td>
    <td style="text-align:center">88</td>
    <td style="text-align:center">63</td>
    <td style="text-align:center">98</td>
  </tr>
    
  <tr>
    <td style="text-align:left"><i>Refrescante</i></td>
    <td style="text-align:center">60</td>
    <td style="text-align:center">85</td>
    <td style="text-align:center">73</td>
    <td style="text-align:center">78</td>
  </tr>
    
  <tr>
    <td style="text-align:left"><i>Light</i></td>
    <td style="text-align:center">50</td>
    <td style="text-align:center">55</td>
    <td style="text-align:center">82</td>
    <td style="text-align:center">91</td>
  </tr>
    
</table>

<p style="text-align: center;"><b>Tabla 3. Litros disponibles de cada fruta</b></p>

<table class="egt">
    
  <tr>  
    <th style="text-align:center">Frutas</th> 
    <th style="text-align:center">Litros disponibles</th>
  </tr>
    
  <tr>
    <td style="text-align:center"><i>Piña</i></td>
    <td style="text-align:center">4,318</td>
  </tr>
    
  <tr>
    <td style="text-align:center"><i>Guayaba</i></td>
    <td style="text-align:center">1,902</td>
  </tr>
    
  <tr>
    <td style="text-align:center"><i>Nispero</i></td>
    <td style="text-align:center">2,683</td>
  </tr>
    
  <tr>
    <td style="text-align:center"><i>Zapote</i></td>
    <td style="text-align:center">1,111</td>
  </tr>
    
</table>

<p style="text-align: center;"><b>Tabla 4. Demanda mínima y precio de cada jugo</b></p>

<table class="egt">
    
  <tr>  
    <th style="text-align:center">Jugos</th> 
    <th style="text-align:center">Demanda mínima</th>
    <th style="text-align:center">Precio</th>
  </tr>
    
  <tr>
    <td style="text-align:center"><i>Saludable</i></td>
    <td style="text-align:center">1,200</td>
    <td style="text-align:center">9,000</td>
  </tr>
    
  <tr>
    <td style="text-align:center"><i>Tropical</i></td>
    <td style="text-align:center">925</td>
    <td style="text-align:center">5,000</td>
  </tr>
    
  <tr>
    <td style="text-align:center"><i>Mañanero</i></td>
    <td style="text-align:center">1,865</td>
    <td style="text-align:center">6,000</td>
  </tr>
    
  <tr>
    <td style="text-align:center"><i>Colombiano</i></td>
    <td style="text-align:center">1,035</td>
    <td style="text-align:center">10,000</td>
  </tr>
    
  <tr>
    <td style="text-align:center"><i>Refrescante</i></td>
    <td style="text-align:center">2,231</td>
    <td style="text-align:center">7,000</td>
  </tr>
    
  <tr>
    <td style="text-align:center"><i>Light</i></td>
    <td style="text-align:center">1,353</td>
    <td style="text-align:center">8,000</td>
  </tr>
    
</table>

Usted debe formular un programa lineal que le permita OptiJuice responder la siguiente pregunta: ¿Cuántos litros de zumo de cada fruta se deben mezclar para producir cada uno de los tipos de jugos, de manera que se cumplan las condiciones previamente expuestas y se maximicen los ingresos totales?

## Formulación

### Variables de Decisión

**a.** Describa la(s) variable(s) de decisión que utilizará en el modelo. 

\begin{align*}
x_{ki}: \text{cantidad (en litros) del zumo de la fruta $i\in R$ destinados a la producción del jugo de tipo $k\in K$}
\end{align*}

### Restricciones

**b.** Escriba la(s) restricción(es) lineal(es) que describe(n) que el jugo del tipo $k\in K$ debe contener entre un $l_{ki}$% y un $u_{ki}$% de litros de zumo de la fruta $i\in R$. 

\begin{align*}
x_{ki} &\ge l_{ki}\%\sum_{j\in R} x_{kj}, &&\forall k\in K,i\in R;\\
x_{ki} &\le u_{ki}\%\sum_{j\in R} x_{kj}, &&\forall k\in K,i\in R.
\end{align*}

**c.** Escriba la(s) restricción(es) que describe(n) que OptiJuice puede utilizar máximo $b_i$ litros de zumo de la fruta $i\in R$. 

\begin{align*}
\sum_{k\in K} x_{ki} &\le b_i, &&\forall i\in R.
\end{align*}

**d.** Escriba la(s) restricción(es) que describe(n) que OptiJuice desea cumplir con la demanda mínima de $d_k$ litros jugo del tipo $k\in K$. 

\begin{align*}
\sum_{i\in R} x_{ki} &\ge d_k, &&\forall k\in K.
\end{align*}

### Naturaleza de las Variables
**e.** Escriba la(s) restricción(es) que describe(n) matemáticamente el tipo de variable(s) que está utilizando dentro del modelo. 

\begin{align*}
x_{ki} & \ge 0, &&\forall k\in K,i\in R.
\end{align*}

### Función Objetivo

**f.** Escriba la función objetivo que maximiza los ingresos totales.

$$
\text{maximizar }  \sum_{k\in K}\sum_{i\in R}p_kx_{ki}
$$

## Formulación matemática

**Conjuntos:**

- $K$: Jugos autóctonos
- $R$: Frutas tropicales

**Parámetros:**

- $l_{ki}$%: porcentaje mínimo de litros de zumo de la fruta $i\in R$ que tiene que tener el jugo del tipo $k\in K$
- $u_{ki}$%: porcentaje máximo de litros de zumo de la fruta $i\in R$ que tiene que tener el jugo del tipo $k\in K$
- $b_i$: litros de zumo de la fruta $i\in R$ disponibles
- $d_k$: demanda mínima (en litros) del jugo de tipo $k\in K$ 
- $p_k$: precio de un litro del jugo de tipo $k\in K$

**Variables de decisión:**

- $x_{ki}$: cantidad (en litros) del zumo de la fruta $i\in R$ destinados a la producción del jugo de tipo $k\in K$

**Modelo:**

$$
\text{maximizar }  \sum_{k\in K}\sum_{i\in R}p_kx_{ki} \text{ (1)} 
$$

Sujeto a,
\begin{align*}
x_{ki} &\ge l_{ki}\%\sum_{j\in R} x_{kj}, &&\forall k\in K,i\in R; &(2)\\
x_{ki} &\le u_{ki}\%\sum_{j\in R} x_{kj}, &&\forall k\in K,i\in R; &(3)\\
\sum_{k\in K} x_{ki} &\le b_i, &&\forall i\in R; &(4)\\
\sum_{i\in R} x_{ki} &\ge d_k, &&\forall k\in K; &(5)\\
x_{ki} & \ge 0, &&\forall k\in K,i\in R. &(6)
\end{align*}

La función objetivo (1) maximiza los ingresos totales. Las restricciones (2) y (3) describen que el jugo del tipo $k\in K$ debe contener entre un $l_{ki}$% y un $u_{ki}$% de litros de zumo de la fruta $i\in R$. La restricción (4) describe que OptiJuice puede utilizar máximo $b_i$ litros de zumo de la fruta $i\in R$. La restricción (5) describe que OptiJuice desea cumplir con la demanda mínima de $d_k$ litros jugo del tipo $k\in K$. La restricción (6) describe la naturaleza de la variable $x_{ki}$. 

## Implementación

**g.** Resuelva el modelo planteado utilizando la librería de PulP en Python. ¿Cuál es la solución
óptima del problema? 

#se importa la libreria de PulP
import pulp as lp

#-----------------
# Conjuntos
#-----------------
#Jugos
K=["Saludable", 
   "Tropical", 
   "Mañanero", 
   "Colombiano", 
   "Refrescante", 
   "Light"]

#Frutas
R=["Piña", 
   "Guayaba", 
   "Níspero", 
   "Zapote"]

# Conjunto con todas las duplas (pozo,tiempo)
K_x_R = [(jugo, fruta) for jugo in K for fruta in R] 

#-----------------
# Parámetros
#-----------------
l={#(jugo, fruta): porcentaje mínimo de litros de la fruta i en el jugo k
   ("Saludable", "Piña"):0.32,
   ("Saludable", "Guayaba"):0.27, 
   ("Saludable", "Níspero"):0.12, 
   ("Saludable", "Zapote"):0.13, 
   ("Tropical", "Piña"):0.18, 
   ("Tropical", "Guayaba"):0.30, 
   ("Tropical", "Níspero"):0.31, 
   ("Tropical", "Zapote"):0.34, 
   ("Mañanero", "Piña"):0.07, 
   ("Mañanero", "Guayaba"):0.31, 
   ("Mañanero", "Níspero"):0.28, 
   ("Mañanero", "Zapote"):0.22, 
   ("Colombiano", "Piña"):0.11, 
   ("Colombiano", "Guayaba"):0.05,
   ("Colombiano", "Níspero"):0.15,
   ("Colombiano", "Zapote"):0.18,
   ("Refrescante", "Piña"):0.46,
   ("Refrescante", "Guayaba"):0.50,
   ("Refrescante", "Níspero"):0.02,
   ("Refrescante", "Zapote"):0.43,
   ("Light", "Piña"):0.36,
   ("Light", "Guayaba"):0.19,
   ("Light", "Níspero"):0.14,
   ("Light", "Zapote"):0.40} 

u={#(jugo, fruta): porcentaje máximo de litros de la fruta i en el jugo k
   ("Saludable", "Piña"):0.95,
   ("Saludable", "Guayaba"):0.83, 
   ("Saludable", "Níspero"):0.66, 
   ("Saludable", "Zapote"):0.87, 
   ("Tropical", "Piña"):0.92, 
   ("Tropical", "Guayaba"):0.76, 
   ("Tropical", "Níspero"):0.69, 
   ("Tropical", "Zapote"):0.56, 
   ("Mañanero", "Piña"):0.81, 
   ("Mañanero", "Guayaba"):0.61, 
   ("Mañanero", "Níspero"):0.28, 
   ("Mañanero", "Zapote"):0.94, 
   ("Colombiano", "Piña"):0.82, 
   ("Colombiano", "Guayaba"):0.88,
   ("Colombiano", "Níspero"):0.63,
   ("Colombiano", "Zapote"):0.98,
   ("Refrescante", "Piña"):0.60,
   ("Refrescante", "Guayaba"):0.85,
   ("Refrescante", "Níspero"):0.73,
   ("Refrescante", "Zapote"):0.78,
   ("Light", "Piña"):0.50,
   ("Light", "Guayaba"):0.55,
   ("Light", "Níspero"):0.82,
   ("Light", "Zapote"):0.91} 

b={#fruta: litros disponibles de la fruta i
   "Piña":4318, 
   "Guayaba":1902, 
   "Níspero":2683, 
   "Zapote":1111}  

d={#jugo: demanda del jugo k
   "Saludable":1200, 
   "Tropical":925, 
   "Mañanero":1865, 
   "Colombiano":1035, 
   "Refrescante":2231, 
   "Light":1353} 

p={#jugo: precio del jugo k
   "Saludable":9000, 
   "Tropical":5000, 
   "Mañanero":6000, 
   "Colombiano":10000, 
   "Refrescante":7000, 
   "Light":8000} 

#-------------------------------------
# Creación del objeto problema en PuLP
#-------------------------------------
#Crea el problema para cargarlo con la instancia 
problema=lp.LpProblem("OptiJuice",lp.LpMaximize)

#-----------------------------
# Variables de Decisión
#-----------------------------
x=lp.LpVariable.dicts('x',K_x_R,lowBound=0,cat='Continuous') #litros de la fruta i para producir el jugo k, aca se añade de una vez la naturaleza de las variables

#-----------------------------
# Función objetivo
#-----------------------------
#Crea la expresión de maximización de ingresos
problema+=lp.lpSum(p[k]*x[k,i] for k in K for i in R), "Ingresos Totales"

#-----------------------------
# Restricciones
#-----------------------------
for k in K:
    for i in R:
        #x_ki >= l_ki*sum(j in R)x_kj forall k in K, i in R
        problema+= x[k,i] >= l[k,i]*lp.lpSum(x[k,j] for j in R), "Mínimo fruta "+i +" -jugo "+k  #se garantiza el mínimo de fruta i en el jugo k
        
        #x_ki <= u_ki*sum(j in R)x_kj forall k in K, i in R
        problema+= x[k,i] <= u[k,i]*lp.lpSum(x[k,j] for j in R), "Máximo fruta "+i +" -jugo "+k  #se garantiza el máximo de fruta i en el jugo k

#sum(k in K)x_ki <= b_i forall i in R
for i in R:
    problema+= lp.lpSum(x[k,i] for k in K) <= b[i], "límite fruta "+i #se garantiza que no se utilice más fruta de la que hay disponible

#sum(i in R)x_ki <= d_k forall k in K
for k in K:
    problema+= lp.lpSum(x[k,i] for i in R) <= d[k], "Demanda mínima jugo "+k #se satisface la demanda
    
#-----------------------------
# Imprimir formato LP
#-----------------------------
#Escribe el problema en un archivo con formato LP 
problema.writeLP("OptiJuice.lp")

#-----------------------------
# Invocar el optimizador
#-----------------------------
#Optimizar el modelo con CBC (default de PuLP)
problema.solve()

#-----------------------------
#    Imprimir resultados
#-----------------------------
#Imprimir estado final del optimizador
print("Estado (optimizador):", lp.LpStatus[problema.status],end='\n')

#Valor óptimo de la función objetivo   
print("\nOptiJuice - Ingresos totales = $", round(lp.value(problema.objective),2))
print()

#Imprimir variables de decisión
print("Variables de decisión")
print("              ","Piña", "Guayaba", "Níspero", "Zapote",sep='\t')
for k in K:
    print(k,round(x[k,"Piña"].value(),2),round(x[k,"Guayaba"].value(),2),round(x[k,"Níspero"].value(),2),round(x[k,"Zapote"].value(),2),sep='\t')






## Créditos

Desarrollo: Juan Felipe Rengifo M<br>
Fecha: 05/09/2020